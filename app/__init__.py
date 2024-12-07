from flask import Flask
from .extentions import db, ma
from .routes import main_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    app.config.from_pyfile('config.py', silent=True)  # Load instance-specific config if exists

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Register blueprints
    app.register_blueprint(main_bp)

    return app
