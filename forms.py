from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class Blogform(FlaskForm):
    title = StringField('Title of Blog', validators=[InputRequired(), Length(max=100)])
    content = TextAreaField("Enter your Content here", validators=[InputRequired(), Length(max=2000)])
    author = StringField('Enter your Name', validators=[InputRequired(), Length(max=100)])
    author_designation = StringField('enter your post', validators=[InputRequired(), Length(max=100)])
    submit = SubmitField('Post')


class MembershipForm(FlaskForm):
    names = StringField('Full Name', validators=[InputRequired(), Length(max=100)])
    enrollment = IntegerField('Enrollment Number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    branch = SelectField('Branch', choices=[('Computer Science 1', 'CS1'), ('Computer Science 2', 'CS2'),
                                            ('Computer Science 3', 'CS3'), ('Computer Science 4', 'CS4'),
                                           ('Computer Science 5', 'CS5'), ('Information Technology 1', 'IT1'),
                                            ('Information Technology 2', 'IT2'), ('Data Science', 'DS'),
                                            ('Internet of things', 'IoT'),
                                            ('Computer Science and Information Technology 1', 'CSIT1'),
                                            ('Computer Science and Information Technology 2', 'CSIT2'),
                                            ('Computer Science and Information Technology 3', 'CSIT3')])
    year = SelectField('Year',
                       choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')])
    interest = StringField('Interest', validators=[InputRequired(), Length(max=100)])
    reason = TextAreaField('Reason for Interest', validators=[InputRequired(), Length(max=500)])
    submit= SubmitField('Submit')

class Messageform(FlaskForm):
    names = StringField('Full Name', validators=[InputRequired(), Length(max=100)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired(), Length(max=100)])
    message = TextAreaField('Message', validators=[InputRequired(), Length(max=500)])
    submit=SubmitField('submit')
