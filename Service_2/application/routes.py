from application import app
import random


@app.route('/randomnumber', methods=['GET'])
def beginning():

	list = ['1','2','3','4','5','6','7']
	
	return list[random.randrange(6)]