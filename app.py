from flask import Flask, flash, render_template, request
import os
from src import validator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

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
