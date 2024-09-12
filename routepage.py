from flask import Flask, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError
import docs
from models import db,Blog, Message, Membership
from forms import Blogform, Messageform, MembershipForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dsac.db'
app.config['SECRET_KEY'] = 'atworkofdsac'
db.init_app(app)


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
        return redirect(url_for('home'))

    return render_template('index.html', form=form, docs=docs)
@app.route('/membership', methods=['GET', 'POST'])
def membership():
    form = MembershipForm()

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
            db.session.add(Membership(name=name, enrollment=enrollment, email=email, branch=branch, year=year,
                                      interest=interest, reason=reason)
                           )
            db.session.commit()
            flash('Your membership request has been submitted', 'success')
            return redirect(url_for('home'))
        except IntegrityError as e:
            db.session.rollback()
            flash('An integrity error occurred. This email address is already in use.', 'error')
    return render_template('membership.html', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = Blogform()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author = form.author.data
        author_designation = form.author_designation.data
        new_post = Blog(title=title, content=content, author=author, author_designation=author_designation)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('createblog.html', form=form)


@app.route('/show_post')
def show_post():
    posts = Blog.query.all()
    print(posts)
    return render_template('readblog.html', posts=posts)
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('post.html', post=post)


with app.app_context():
    db.create_all()
app.run(debug=True, port=8000)
