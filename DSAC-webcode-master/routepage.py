
from flask import Flask ,render_template,redirect,flash


app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)