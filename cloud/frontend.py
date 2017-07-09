"""Creates autoscaled, network LB IGM running specified docker image."""


def GenerateConfig(context):
  """Generate YAML resource configuration."""

  # Pull the region out of the zone
  region = context.properties['zone'][:context.properties['zone'].rfind('-')]
  name = context.env['name']

  resources = [{
      'name': name,
      'type': 'container_instance_template.py',
      'properties': {
          'port': context.properties['port'],
          'dockerEnv': context.properties['dockerEnv'],
          'dockerImage': context.properties['dockerImage'],
          'containerImage': context.properties['containerImage']
      }
  }, {
      'name': name + '-igm',
      'type': 'compute.v1.instanceGroupManager',
      'properties': {
          'zone': context.properties['zone'],
          'targetSize': context.properties['size'],
          'targetPools': ['$(ref.' + name + '-tp.selfLink)'],
          'baseInstanceName': name + '-instance',
          'instanceTemplate': '$(ref.' + name + '-it.selfLink)'
      }
  }, {
      'name': name + '-as',
      'type': 'compute.v1.autoscaler',
      'properties': {
          'zone': context.properties['zone'],
          'target': '$(ref.' + name + '-igm.selfLink)',
          'autoscalingPolicy': {
              'maxNumReplicas': context.properties['maxSize']
          }
      }
  }, {
      'name': name + '-hc',
      'type': 'compute.v1.httpHealthCheck',
      'properties': {
          'port': context.properties['port'],
          'requestPath': '/gcpoc.php'
      }
  }, {
      'name': name + '-tp',
      'type': 'compute.v1.targetPool',
      'properties': {
          'region': region,
          'healthChecks': ['$(ref.' + name + '-hc.selfLink)']
      }
  }, {
      'name': name + '-lb',
      'type': 'compute.v1.forwardingRule',
      'properties': {
          'region': region,
          'portRange': context.properties['port'],
          'target': '$(ref.' + name + '-tp.selfLink)'
      }
  }]
  return {'resources': resources}
