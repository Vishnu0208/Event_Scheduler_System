
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models.resource import Resource

resource_bp = Blueprint('resources', __name__)

@resource_bp.route('/resources')
def list_resources():
    return render_template('resources/list.html', resources=Resource.query.all())

@resource_bp.route('/resources/add', methods=['GET','POST'])
def add_resource():
    if request.method == 'POST':
        r = Resource(name=request.form['name'], type=request.form['type'])
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('resources.list_resources'))
    return render_template('resources/add.html')
