
from app import create_app, db
from models.resource import Resource
from models.event import Event
from datetime import datetime

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add_all([
        Resource(name='Room A', type='Room'),
        Resource(name='Room B', type='Room'),
        Resource(name='Projector', type='Equipment')
    ])

    db.session.add_all([
        Event(title='Workshop', start_time=datetime(2025,1,1,10), end_time=datetime(2025,1,1,12)),
        Event(title='Seminar', start_time=datetime(2025,1,1,11), end_time=datetime(2025,1,1,13))
    ])

    db.session.commit()
    print("Seed data inserted")
