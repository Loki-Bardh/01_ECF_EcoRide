import os
from flask import Flask
from app.models.postgres import db
from mongoengine import connect
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

def create_app():
    app = Flask(__name__)

    # Flask Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["DEBUG"] = True

    # PostgreSQL Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
