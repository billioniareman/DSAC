from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dsac.db'
app.config['SECRET_KEY'] = 'atworkofdsac'
db = SQLAlchemy(app)


class Membership(db.Model):
    name = db.Column(db.String, nullable=False)
    enrollment = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    branch = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    interest = db.Column(db.String, nullable=False)
    reason = db.Column(db.String, nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    subject = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)


class MyForm(FlaskForm):
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


class Messageform(FlaskForm):
    names = StringField('Full Name', validators=[InputRequired(), Length(max=100)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired(), Length(max=100)])
    message = TextAreaField('Message', validators=[InputRequired(), Length(max=500)])


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Messageform()

    if form.validate_on_submit():
        name = form.names.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        # Create a Message object and add it to the database
        message_to_database = Message(name=name, email=email, subject=subject, message=message)
        db.session.add(message_to_database)
        db.session.commit()
        flash('Your message has been sent to the team', 'success')
        return redirect('/')

    return render_template('index.html', form=form)


@app.route('/membership', methods=['GET', 'POST'])
def membership():
    form = MyForm()

    if form.validate_on_submit():
        name = form.names.data
        enrollment = form.enrollment.data
        email = form.email.data
        branch = form.branch.data
        year = form.year.data
        interest = form.interest.data
        reason = form.reason.data
        try:
            # Create a Membership object and add it to the database
            membership = Membership(name=name, enrollment=enrollment, email=email, branch=branch, year=year,
                                    interest=interest, reason=reason)
            db.session.add(membership)
            db.session.commit()
            flash('Your membership request has been submitted', 'success')
            return redirect('home')
        except IntegrityError as e:
            db.session.rollback()
            flash('An integrity error occurred. This email address is already in use.', 'error')
    return render_template('membership.html', form=form)


with app.app_context():
    db.create_all()
app.run(debug=True, port=8000)
