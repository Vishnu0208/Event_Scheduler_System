
from models.event import Event
from models.allocation import EventResourceAllocation
from app import db

def has_conflict(resource_id, start, end, event_id=None):
    q = db.session.query(Event).join(EventResourceAllocation).filter(
        EventResourceAllocation.resource_id == resource_id,
        Event.start_time < end,
        Event.end_time > start
    )
    if event_id:
        q = q.filter(Event.id != event_id)
    return q.first() is not None
