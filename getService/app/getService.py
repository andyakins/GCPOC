import connexion

app = connexion.App(__name__, 8080, specification_dir='api/')
app.add_api('getService.yaml', resolver=RestyResolver('api'))
app.run()
