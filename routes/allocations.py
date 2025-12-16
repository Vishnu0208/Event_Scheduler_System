
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.event import Event
from models.resource import Resource
from models.allocation import EventResourceAllocation
from utils.conflict_checker import has_conflict

allocation_bp = Blueprint('allocations', __name__)

@allocation_bp.route('/allocate', methods=['GET','POST'])
def allocate():
    events = Event.query.all()
    resources = Resource.query.all()

    if request.method == 'POST':
        event = Event.query.get(request.form['event_id'])
        resource_id = int(request.form['resource_id'])

        if has_conflict(resource_id, event.start_time, event.end_time):
            flash("Conflict detected!")
        else:
            db.session.add(EventResourceAllocation(
                event_id=event.id,
                resource_id=resource_id
            ))
            db.session.commit()
            flash("Allocated successfully")

    return render_template('allocations/allocate.html', events=events, resources=resources)
