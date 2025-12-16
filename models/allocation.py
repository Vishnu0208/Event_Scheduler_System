
from app import db

class EventResourceAllocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
