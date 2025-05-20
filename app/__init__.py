import os
from flask import Flask
from dotenv import load_dotenv
from app.models.models_postgres import db
from mongoengine import connect

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # PostgreSQL Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URI")  # Store URI in .env
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # MongoDB Connection
    connect(
        db=os.getenv("MONGO_DB_NAME", "ecoride_reviews"),
        host=os.getenv("MONGO_URI", "localhost"),
        port=int(os.getenv("MONGO_PORT", 27017))
    )

    # Register all route blueprints
    from app.routes import register_routes
    register_routes(app)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
