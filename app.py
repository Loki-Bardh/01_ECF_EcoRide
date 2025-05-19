import os
from flask import Flask, render_template
from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy
#from flask_pymongo import PyMongo
from app import create_app

app = create_app()

# PostgreSQL config
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URI")
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

# MongoDB config
#app.config["MONGO_URI"] = os.getenv("MONGO_URI")
#mongo = PyMongo(app)

# Example SQLAlchemy model
#class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(50), nullable=False)

@app.route("/")
def accueil():
    # Query PostgreSQL
    #users = User.query.all()

    # Query MongoDB collection
    #mongo_users = mongo.db.users.find()  # assuming a 'users' collection

    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
