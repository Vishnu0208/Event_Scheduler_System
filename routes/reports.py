
from flask import Blueprint, render_template, request
from datetime import datetime
from models.resource import Resource

report_bp = Blueprint('reports', __name__)

@report_bp.route('/report', methods=['GET','POST'])
def report():
    data = []
    if request.method == 'POST':
        start = datetime.fromisoformat(request.form['start'])
        end = datetime.fromisoformat(request.form['end'])
        for r in Resource.query.all():
            hours = 0
            for a in r.eventresourceallocation_set if hasattr(r,'eventresourceallocation_set') else []:
                e = a.event
                if e.start_time >= start and e.end_time <= end:
                    hours += (e.end_time - e.start_time).seconds / 3600
            data.append((r.name, hours))
    return render_template('reports/utilisation.html', data=data)
