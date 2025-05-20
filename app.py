
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


if __name__ == "__main__":
    app.run(debug=False)
