from flask import Flask, flash, render_template, request, jsonify
import os
from src import validator
import json
from decimal import Decimal

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():

	f = open('./data/pstatus', 'r')
	processed = f.read()
	f.close()

	n = int(processed)
	total = len(os.listdir('./data/resume_dataset/'))

	for i in range(n + 1, total + 1):
		validator.resume_score(str(i))
		print(i)

	f = open('./data/pstatus', 'w')
	f.write(str(total))
	f.close()

	return "preprocessing complete\n" + str(n) + " entries pushed to redis"

@app.route('/<i>', methods=['GET', 'POST'])
def giveMeJSON(i):
	curr_resume = "resume" + str(i)
	result = json.loads(r.get(curr_resume).decode('utf8').replace("'", '"'))
	print(type(result))
	return jsonify(result)

@app.route('/checker', methods=['GET', 'POST'])
def checker():

	if request.method == 'POST' and 'cgpa' in request.form and 'college' in request.form and 'skill' in request.form:
		cgpa = request.form['cgpa']
		college = request.form['college']
		skill = request.form['skill']

		#print(cgpa)
		#print(college)
		#print(skill)	
		n = 44

		chosen_resume = []

		for i in range(1, n + 1):
			status, file = validator.resume_score(cgpa, str(college), str(skill), str(i))
			if(status):
				chosen_resume.append(file)

		print(chosen_resume)

		return render_template('index.html', files=chosen_resume)
	else:
		return render_template('index.html')


if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)
