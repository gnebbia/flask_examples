import os
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session, logging
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
# Flask is the fundamental import
# jsonify allows us to build jsons from maps
# request allows us to receive jsons

basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)


# This is the CSRF Key
app.config['SECRET_KEY'] = 'mykey'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Puppy(db.Model):

    # manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"




@app.route('/')
def index():
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


if __name__=="__main__":
    # Deployment
    #app.run(host='127.0.0.1', port=80)
    # Development
    app.run(debug=True)


