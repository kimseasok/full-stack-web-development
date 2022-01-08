from app import app_factory, app, DevConfig

current_app, db = app_factory(app, config=DevConfig)


current_app.run(debug=True, port=5000)