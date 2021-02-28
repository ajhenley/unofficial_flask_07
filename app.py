from flask import Flask
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(application)

from routes import app

application.register_blueprint(app)

from app import db
db.create_all()

if __name__ == '__main__':
    app.run()
