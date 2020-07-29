from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomriddle')
    print(response)
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')