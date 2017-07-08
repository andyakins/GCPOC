import connexion

app = connexion.FlaskApp(__name__, specification_dir='api/')
app.add_api('getService.yaml')
app.run(port=8080)
