from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session, logging
from data import Articles
from passlib.hash import sha256_crypt
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from wtforms import (Form, StringField, TextAreaField, PasswordField, 
                     BooleanField, DateTimeField, RadioField,
                     SelectField, TextField, SubmitField, validators)
# Flask is the fundamental import
# jsonify allows us to build jsons from maps
# request allows us to receive jsons

# ref. 71

app = Flask(__name__)


# This is the CSRF Key
app.config['SECRET_KEY'] = 'mykey'

# Class representing form way 1
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=20)])
    username = StringField('Username', [validators.Length(min=4, max=10)])
    email = StringField('Email', [validators.Length(min=5, max=70)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
        ])
    confirm = PasswordField("Confirm Password")



@app.route('/register1', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        return render_template('register.html', form=form)

    return render_template('register.html', form=form)



# Class representing form way 2
class RegisterForm2(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    sex = BooleanField("Are you male?")
    mood = RadioField("Choose your mood:",
                      choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField('Pick your favorite food:',
                      choices=[('chi','Chicken'),('bf','Beef')])
    feedback = TextAreaField()
    
    submit = SubmitField('Submit')



@app.route('/register2', methods=['GET', 'POST'])
def register2():
    form = RegisterForm2()
    if form.validate_on_submit():
        session['name']        = form.name.data
        session['sex']         = form.sex.data
        session['mood']        = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback']    = form.feedback.data

        return redirect(url_for('thanks'))

    return render_template('register2.html', form=form)





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


