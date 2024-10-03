from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_description = TextAreaField('Event Description', validators=[DataRequired()])
    event_date = DateField('Event Date', validators=[DataRequired()])
    event_start_time = TimeField('Start Time', validators=[DataRequired()])
    event_end_time = TimeField('End Time', validators=[DataRequired()])
    latitude = HiddenField('Latitude', validators=[DataRequired()])
    longitude = HiddenField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Create Event')
