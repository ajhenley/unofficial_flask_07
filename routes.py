from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

from models import Person
from app import db

@app.route('/')
def index():
    people = Person.query.all()
    return render_template("index.html", people = people)


@app.route('/add')
def add():
    return render_template("form.html")


@app.route('/processform', methods=['GET','POST'])
def processform():
    firstname = request.form['first']
    lastname = request.form['last']
    person = Person(firstname,lastname)
    db.session.add(person)
    db.session.commit()
    return redirect(url_for('index'))