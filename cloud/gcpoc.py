def GenerateConfig(context):
  """Generate configuration."""

  database = context.env['deployment'] + '-database'
  frontend = context.env['deployment'] + '-frontend'
  getservice = context.env['deployment'] + '-getservice'
  postservice = context.env['deployment'] + '-postservice'
  firewall = context.env['deployment'] + '-firewall'
  network = context.env['deployment'] + '-network'
  application_port = 80
  mysql_port = 3306
  get_port = 8080
  post_port = 8081
  resources = [
    {
      'name': database,
      'type': 'container_vm.py',
      'properties': {
        'zone': context.properties['zone'],
        'dockerImage': 'andyakins/gcpocdb',
        'containerImage': 'family/container-vm',
        'port': mysql_port,
      }
    },
    {
      'name': getservice,
      'type': 'container_vm.py',
      'properties': {
        'zone': context.properties['zone'],
        'dockerImage': 'andyakins/gcpocget',
        'containerImage': 'family/container-vm',
        'dockerEnv': {
          'GCPOC_DB_HOST':'$(ref.' + database + '.networkInterfaces[0].networkIP)',
          'GCPOC_DB_USER':'GCPOC',
          'GCPOC_DB_PASSWORD':'GCPOCPassword',
          'GCPOC_DB_DATABASE':'GCPOC',
          'GOOGLE_APPLICATION_CREDENTIALS':'/gcpoc/credentials.json'
        },
        'port': get_port
      }
    },
    {
      'name': postservice,
      'type': 'container_vm.py',
      'properties': {
        'zone': context.properties['zone'],
        'dockerImage': 'andyakins/gcpocpost',
        'containerImage': 'family/container-vm',
        'dockerEnv': {
          'GCPOC_DB_HOST':'$(ref.' + database + '.networkInterfaces[0].networkIP)',
          'GCPOC_DB_USER':'GCPOC',
          'GCPOC_DB_PASSWORD':'GCPOCPassword',
          'GCPOC_DB_DATABASE':'GCPOC'
        },
        'port': post_port
      }
    },
    {
      'name': frontend,
      'type': 'frontend.py',
      'properties': {
        'zone': context.properties['zone'],
        'dockerImage': 'andyakins/gcpocfront',
        'containerImage': 'family/container-vm',
        'port': application_port,
        'dockerEnv': {
          'GCPOC_GET_URI':'http://$(ref.' + getservice + '.networkInterfaces[0].networkIP):8080/v1.0/list',
          'GCPOC_POST_URI':'http://$(ref.' + postservice + '.networkInterfaces[0].networkIP):8081/v1.0/add'
        },
        'size': 2,
        'maxSize': 20
      }
    },
    {
      'name': firewall,
      'type': 'compute.v1.firewall',
      'properties': {
        'allowed': [{
          'IPProtocol': 'TCP',
          'ports': [application_port]
        },],
        'sourceRanges': ['0.0.0.0/0']
      }
    }
  ]
  return {'resources': resources}
