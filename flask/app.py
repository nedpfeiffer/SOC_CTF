# import the Flask class from the flask module
from flask import Flask, render_template, request, send_file # redirect, url_for, 

# create the application object
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    path = "eps1.0_hellofriend.txt"
    if request.method == 'POST':
        if request.form['username'] != 'ealderson' or request.form['password'] != 'qwerty123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return send_file(path, as_attachment=True)
    return render_template('login.html', error=error)

