# app/models/models_mongo.py

from mongoengine import Document, StringField, IntField, ReferenceField, DateTimeField
from datetime import datetime

class Review(Document):
    meta = {'collection': 'reviews'}

    reviewer_id = StringField(required=True)  # User.id as string
    target_id = StringField(required=True)    # User.id of person being reviewed
    ride_id = StringField()                   # Optional - linked rideshare
    role = StringField(choices=["driver", "passenger"], required=True)

    comment = StringField()
    score = IntField(min_value=1, max_value=5)
    status = StringField(choices=["active", "reported", "deleted"], default="active")
    created_at = DateTimeField(default=datetime.utcnow)
