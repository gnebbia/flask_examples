from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session, logging
from data import Articles
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from wtforms import (Form, StringField, TextAreaField, PasswordField, 
                     BooleanField, DateTimeField, RadioField,
                     SelectField, TextField, SubmitField, validators)
# Flask is the fundamental import
# jsonify allows us to build jsons from maps
# request allows us to receive jsons

# ref. 71

app = Flask(__name__)


Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thank_you.html', first=first, last=last)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/urls')
def urls():
    return render_template('urls.html')

@app.route('/filters/<name>')
def filters(name):
    return render_template('filters.html', name=name)


@app.route('/jinja/')
def jinja():
    simple = "a simple string"
    lista = [1, 4, "ciao"]
    diz = {"animal": "cane",
           "car": "fiat punto",
           "giaggi": "sforfo"}

    return render_template('jinja.html', simple=simple, lista=lista, diz=diz)


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id = id)

@app.route('/names/<name>')
def names(name):
    return "Hello {}".format(name)



@app.route('/hithere')
def hi_there():
    return "Hi am on /hithere"

@app.route('/service1')
def service_one():
    retJson = {
            'field1':'abc',
            'field2':'def'
    }
    return jsonify(retJson)

# by default routes allow only the GET method
# this route allows only POST
@app.route('/add_nums', methods=['POST'])
def add_nums():
    data_dict = request.get_json()

    field1 = data_dict['fieldname1']
    field2 = data_dict['fieldname2']
    z = field1 + field2
    resultDict = { "z": z}
    return jsonify(resultDict), 200 # this is the returned response



# How to create a form with validation
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=20)])
    username = StringField('Username', [validators.Length(min=4, max=10)])
    email = StringField('Email', [validators.Length(min=5, max=70)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
        ])
    confirm = PasswordField("Confirm Password")


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        return render_template('register.html', form=form)

    return render_template('register.html', form=form)


# How to handle errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__=="__main__":
    # Deployment
    #app.run(host='127.0.0.1', port=80)
    # Development
    app.run(debug=True)


