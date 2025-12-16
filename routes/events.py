
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from models.event import Event

event_bp = Blueprint('events', __name__)

@event_bp.route('/')
def index():
    return redirect(url_for('events.list_events'))

@event_bp.route('/events')
def list_events():
    events = Event.query.all()
    return render_template('events/list.html', events=events)

@event_bp.route('/events/add', methods=['GET','POST'])
def add_event():
    if request.method == 'POST':
        e = Event(
            title=request.form['title'],
            start_time=datetime.fromisoformat(request.form['start']),
            end_time=datetime.fromisoformat(request.form['end']),
            description=request.form['description']
        )
        db.session.add(e)
        db.session.commit()
        flash("Event created")
        return redirect(url_for('events.list_events'))
    return render_template('events/add.html')
