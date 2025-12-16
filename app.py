import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure instance path exists
    os.makedirs(os.path.join(os.path.dirname(__file__), 'instance'), exist_ok=True)

    db.init_app(app)

    from routes.events import event_bp
    from routes.resources import resource_bp
    from routes.allocations import allocation_bp
    from routes.reports import report_bp

    app.register_blueprint(event_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(allocation_bp)
    app.register_blueprint(report_bp)

    with app.app_context():
        db.create_all()

    return app
