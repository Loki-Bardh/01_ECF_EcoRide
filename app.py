import os
from flask import Flask, render_template
from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy
#from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

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


if __name__ == "__main__":
    app.run(debug=True)
