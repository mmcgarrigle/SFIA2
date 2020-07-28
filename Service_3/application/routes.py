from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['A','B','C','D','E','F','G']
	
	return list[random.randrange(6)]