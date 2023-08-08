from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)

@app.route('/')
def home():
    return "<style> h1 {color: red; font-family: arial}; </style><h1>Welcome to my web app!</h1>"

@app.route('/postoption')
def posto():
    response = request.method
    return f"method is {response}"

@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    return f"the number {number} squared is {squared}"

@app.route('/gotohome')
def gotohome():
    return redirect(url_for('home'))  # Corrected to use the 'redirect' function

if __name__ == '__main__':
    app.run()
