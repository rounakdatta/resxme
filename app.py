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

    dirs=os.listdir('./data/resume_dataset/')
    print(dirs)
    for i in range(n + 1, total + 1):
        if(dirs[i-1].find("pdf")>0):
            print(dirs[i-1])
            validator.resume_score(str(i))
        elif(dirs[i-1].find("docx")>0):
            print(dirs[i-1])
            validator.resume_score1(str(i))
        print(i)

    f = open('./data/pstatus', 'w')
    f.write(str(total))
    f.close()

    return "preprocessing complete\n" + str(n) + " entries pushed to redis"

@app.route('/<i>', methods=['GET', 'POST'])
def giveMeJSON(i):
    curr_resume = "resume" + str(i)
    result = json.loads(r.get(curr_resume).decode('utf8').replace("'", '"'))
    return jsonify(result)

@app.route('/checker', methods=['GET', 'POST'])
def checker():

    if request.method == 'POST' and 'cgpa' in request.form and 'college' in request.form and 'skill' in request.form:
        cgpa = request.form['cgpa']
        college = request.form['college']
        skill = request.form['skill']

        f = open('./data/pstatus', 'r')
        processed = f.read()
        f.close()
    
        n = int(processed)

        all_resumes = {}
        
        for i in range(1, n + 1):
            point = 0
            curr_resume = "resume" + str(i)
            try:
                print(str(i) + " : ", end="")
                payload = json.loads(r.get(curr_resume).decode('utf8').replace("'", '"'))
                try:
                    if(float(payload["cgpa"] > cgpa)):
                        point += 1
                except:
                    print("", end="")
                try:
                    if(payload["college"] != "null"):
                        point += 1
                except:
                    print("", end="")
                try:
                    sFound = "N"
                    for skill_test in payload["skills"]:
                        if(skill in skill_test.lower()):
                            point += 1
                            sFound = "Y"
                            break
                except:
                    print("", end="")

                print(str(point) + "/3")
                href = os.getcwd() + "/data/resume_dataset/resume" + str(i) + ".pdf"
                all_resumes[str(i)] = {"Points" : point, "CGPA" : float(payload["cgpa"]), "College" : payload["college"], "Skill Found (Y/N)" : sFound, "Location" : href }

            except:
                print("null")

        return jsonify(all_resumes)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
