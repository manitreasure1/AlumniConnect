from .config.config import Config
from .config.dependencies import bcrypt, migrate, jwt_manager, cache, db, compress, cors
from flask import Flask
from .routes.auth import auth_bp


config = Config()

def my_app():
    app = Flask(__name__)
    app.config.from_object(config)
    bcrypt.init_app(app)
    migrate.init_app(app)
    jwt_manager.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    compress.init_app(app)
    cors.init_app(
        app,
        resources={
            r"/api/*": {"origins": "*"}
            }, 
            allow_headers=['Content-Type', 'Authorization'],
            methods=['GET', 'POST', 'PUT', 'DELETE'],
            max_age=3600
            )
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
    





   



