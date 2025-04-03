from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Importar rutas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
