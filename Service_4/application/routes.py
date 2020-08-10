from application import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random
from os import environ

db = SQLAlchemy(app)

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

class Riddles(db.Model):
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    Riddle = db.Column(db.String(1000), nullable=False)
   
    def __repr__(self):
        return ''.join(
            [
                'ID: ' + str(self.id) + '\n' 
                'Riddle: ' + self.riddle
            ]
        )

@app.route('/randomriddle', methods=['GET', 'POST'])
def sentence():
    riddles = {"1A":"Forward I’m heavy, but backwards I’m not. What am I?", "1B":"Add two to eleven and you get one. How is this possible?", "1C":"It’s bought by the yard and worn by the foot. What is it?", "1D":"Something that you have if you don’t share it, but if you do share it you won’t have it.", "1E":"What runs but never gets tired?", "1F":"I lack much reason, but often rhyme, And require logic to pass the time, To get the words to tell your kin, Look for clues that lie within, Though all are different, they act the same, The answer is practically in the name. What am I?", "1G":"Tall in the morning, short at noon, gone at night but I’ll be back soon. What am I?", "2A":"What three letter English word has an odd start, an even finish and an infinitely long middle?", "2B":"With pointed fangs it sits in wait, With piercing force it doles out fate, Over bloodless victims proclaiming its might, Eternally joining in a single bite. What is it?", "2C":"The more you take, the more you leave behind. What am I?", "2D":"What has a head, a tail, is brown, and has no legs?", "2E":"David's father has three sons: Snap, Crackle, and _____?", "2F":"Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?", "2G":"What belongs to you, but other people use it more than you?", "3A":"What comes once in a minute, twice in a moment, but never in a thousand years?", "3B":"You live in a one story house made entirely of redwood. What color would the stairs be?", "3C":"What has many keys, but can't even open a single door?", "3D":"I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "3E":"Re-arrange the letters, O O U S W T D N E J R, to spell just one word. What is it?", "3F":"Mr. and Mrs. Mustard have six daughters and each daughter has one brother. How many people are in the Mustard family?", "3G":"What is more useful when it is broken?", "4A":"I make two people out of one. What am I?", "4B":"What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see?", "4C":"What can point in every direction but can't reach the destination by itself?", "4D":"My life can be measured in hours, I serve by being devoured. Thin, I am quick. Fat, I am slow. Wind is my foe. What am I?", "4E":"What is black when you buy it, red when you use it, and gray when you throw it away?", "4F":"A man rode out of town on Sunday, he stayed a whole night at a hotel and rode back to town the next day on Sunday. How is this possible?", "4G":"I am white when I am dirty, and black when I am clean. What am I?", "5A":"They have not flesh, nor feathers, nor scales, nor bone. Yet they have fingers and thumbs of their own. What are they?", "5B":"As light as a feather, yet no man can hold me for long. What am I?", "5C":"What runs around the whole yard without moving?", "5D":"I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I?", "5E":"Before Mount Everest was discovered, what was the highest mountain on Earth?", "5F":"What's at least 6 inches long, goes in your mouth, and is more fun if it vibrates?", "5G":"The more you take away, the more I become. What am I?", "6A":"What can you catch but never throw?", "6B":"How do you make the number 7 an even number without addition, subtraction, multiplication, or division?", "6C":"I have two hands, but I can not scratch myself. What am I?", "6D":"Poor people have it. Rich people need it. If you eat it you die. what is it?", "6E":"What goes up but never comes down?", "6F":"What goes up when the rain comes down?", "6G":"I have no feet, no hands, no wings, but I climb to the sky. What am I?", "7A":"I am full of holes but I can still hold water. What am I?", "7B":"What 7 letter word is spelled the same way backwards and forwards?", "7C":"I can be cracked, I can be made. I can be told, I can be played. What am I?", "7D":"If eleven plus two equals one, what does nine plus five equal?", "7E":"What are moving left to right, right now?", "7F":"What 4-letter word can be written forward, backward or upside down, and can still be read from left to right?", "7G":"If a rooster laid a brown egg and a white egg, what kind of chicks would hatch?",}
    number = requests.get('http://service_2:5001/randomnumber')
    letter = requests.get('http://service_3:5002/randomletter')
    # number = requests.get('http://localhost:5001/randomnumber')
    # letter = requests.get('http://localhost:5002/randomletter')
    code = number.text + letter.text
    riddle = (riddles[code])
    return riddle

    