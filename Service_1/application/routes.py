from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random
from os import environ


db = SQLAlchemy(app)

# SECRET_KEY = os.urandom(16)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')


class riddles(db.Model):
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    Riddle = db.Column(db.String(1000), nullable=False)
   
    def __repr__(self):
        return ''.join(
            [
                'ID: ' + str(self.ID) + '\n' 
                'Riddle: ' + self.Riddle
            ]
        )


@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service_4:5003/randomriddle')
    # response = requests.get('http://localhost:5003/randomriddle')
    print(response)
    sentence = response.text
    post_data = riddles.query.order_by(riddles.ID.desc()).limit(10).all()
    db.session.add(riddles(Riddle = sentence))
    db.session.commit()
    return render_template('index.html', sentence = sentence, title = 'Home', riddles = post_data)