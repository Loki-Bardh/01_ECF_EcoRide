import os
from flask import Flask
from app.models.postgres import db
from mongoengine import connect
from pathlib import Path
from dotenv import load_dotenv

# Load .env once
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize PostgreSQL
    db.init_app(app)

    # Initialize MongoDB (optional: defer connect)
    connect(
        db=os.getenv("MONGO_DB_NAME", "ecoride_reviews"),
        host=os.getenv("MONGO_URI", "localhost"),
        port=int(os.getenv("MONGO_PORT", 27017)),
        alias="default"
    )

    # Register routes
    from app.routes import register_routes
    register_routes(app)

    return app
