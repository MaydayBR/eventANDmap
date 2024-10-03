from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Event name
    description = db.Column(db.Text, nullable=False)   # Event description
    date = db.Column(db.Date, nullable=False)          # Event date
    start_time = db.Column(db.Time, nullable=False)    # Event start time
    end_time = db.Column(db.Time, nullable=False)      # Event end time
    latitude = db.Column(db.Float, nullable=False)     # Latitude coordinate
    longitude = db.Column(db.Float, nullable=False)    # Longitude coordinate
    created_at = db.Column(db.DateTime, nullable=False)  # Timestamp
