from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    developer = db.Column(db.String(30))
    price = db.Column(db.REAL)
    age_rating = db.Column(db.Integer)
    orders = db.relationship('Orders',  backref='gamesbr')
    
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(10), unique=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)

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
