# app/models/models_postgres.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class user(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))  # admin, employee, end_user
    end_user_type = db.Column(db.String(50))  # driver, passenger, both

    email = db.Column(db.String(120), unique=True, nullable=False)
    pseudonym = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    telephone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    photo_url = db.Column(db.String(255))
    bio = db.Column(db.Text)

    profile = db.relationship('profile', uselist=False, back_populates="user")
    vehicle = db.relationship('vehicle', back_populates="user", uselist=False)
    rides = db.relationship('rideshare', back_populates="driver")

class profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('user', back_populates="profile")

class vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    fuel_type = db.Column(db.String(30))
    color = db.Column(db.String(30))
    license_plate = db.Column(db.String(20), unique=True)
    first_registration_date = db.Column(db.Date)
    total_spots = db.Column(db.Integer)
    photo_url = db.Column(db.String(255))

    user = db.relationship('user', back_populates="vehicle")

class rideshare(db.Model):
    __tablename__ = 'rideshares'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    departure_location = db.Column(db.String(100))
    arrival_location = db.Column(db.String(100))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    available_spots = db.Column(db.Integer)
    price_per_person = db.Column(db.Float)
    status = db.Column(db.String(30))  # waiting, confirmed, en route, cancelled

    driver = db.relationship('user', back_populates="rides")
    
