from app import app_factory, app, DevConfig

current_app= app_factory(app, config=DevConfig)


if __name__ == "__main__":

    current_app.run(debug=True, port=5000)