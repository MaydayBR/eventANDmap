from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import EventForm
from models import db, Event
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('create_event'))

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        # Retrieve data from the form
        event_name = form.event_name.data
        event_description = form.event_description.data
        event_date = form.event_date.data
        event_start_time = form.event_start_time.data
        event_end_time = form.event_end_time.data
        latitude = float(form.latitude.data)
        longitude = float(form.longitude.data)

        # Create a new Event object
        new_event = Event(
            name=event_name,
            description=event_description,
            date=event_date,
            start_time=event_start_time,
            end_time=event_end_time,
            latitude=latitude,
            longitude=longitude,
            created_at=datetime.utcnow()
        )

        # Save the new event to the database
        db.session.add(new_event)
        db.session.commit()

        flash('Event created successfully!', 'success')
        return redirect(url_for('list_events'))

    if request.method == 'GET':
        # Set default coordinates to Detroit if not provided
        form.latitude.data = 42.3314
        form.longitude.data = -83.0458

    return render_template('create_event.html', form=form)

@app.route('/list_events')
def list_events():
    events = Event.query.all()
    events_data = [{
        'name': event.name,
        'description': event.description,
        'latitude': event.latitude,
        'longitude': event.longitude,
        'date': event.date.strftime('%Y-%m-%d'),
        'start_time': event.start_time.strftime('%H:%M'),
        'end_time': event.end_time.strftime('%H:%M')
    } for event in events]
    return render_template('events_list.html', events=events_data)

if __name__ == '__main__':
    app.run(debug=True)
