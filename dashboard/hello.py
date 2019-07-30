from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session, logging
from passlib.hash import sha256_crypt
import numpy as np
import plotly
import plotly.graph_objs as go
import pandas as pd
import json
from flask_mysqldb import MySQL
from wtforms import (Form, StringField, TextAreaField, PasswordField, 
                     BooleanField, DateTimeField, RadioField,
                     SelectField, TextField, SubmitField, validators)
# Flask is the fundamental import
# jsonify allows us to build jsons from maps
# request allows us to receive jsons

# ref. 71

app = Flask(__name__)



def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Scatter(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_plot2():


    val = [19, 26, 55]
    lab = ['Residential', 'Non-Residential', 'Utility']


    data = [
        go.Pie(
            values= val,
            labels= lab
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('dashboard.html', values=values, labels=labels, legend=legend)


@app.route('/dashboard2')
def dashboard2():
    bar = create_plot()
    pie = create_plot2()
    return render_template('dashboard2.html', plot=bar, plot2=pie)


@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id = id)

@app.route('/names/<name>')
def names(name):
    return "Hello {}".format(name)





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





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__=="__main__":
    # Deployment
    #app.run(host='127.0.0.1', port=80)
    # Development
    app.run(debug=True)


