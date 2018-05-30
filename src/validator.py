from src.extract import scrape_pdf
from src.utils import get_cgpa, get_college, get_skills

import spacy
from nltk.tokenize import sent_tokenize
import subprocess

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

import json
from decimal import Decimal

# helper functions for validating various criteria

def validate_cgpa(cgpa, requirement):

	if(float(cgpa) >= float(requirement)):
		return True

def validate_college(college, requirement, n):

	f = open("./data/college_dataset/" + requirement, 'r')
	college_dataset = f.read().lower().replace(',', '').splitlines()

	college = college.replace(',', '').replace('.', '').replace('–', '').replace('-', '').replace('(', '').replace(')', '')

	for single_college in college_dataset:
		if(single_college in college):
			return True, single_college

	return False, "null"

def validate_skills(skills, requirement):

	if(requirement in skills.replace(',', '').replace('.', '').split()):
		return True

# determine the resume score

def resume_score(req1, req2, req3, n):

	filename = "./data/resume_dataset/resume" + n + ".pdf"
	itemx = scrape_pdf(filename)
	nlp = spacy.load('en_core_web_sm')
	item = nlp(itemx)

	skill_payload = sent_tokenize(itemx)
	
	points = 0
	resume_data = {}
	
	#for item in sentences:
	cgpa = get_cgpa(item)
	skillFound, skills = get_skills(item, req3, n)
	resume_data["skills"] = skills

	if cgpa is not None:
		if(validate_cgpa(cgpa, req1)):
			resume_data["cgpa"] = cgpa
			points += 1

	def check_college(payload):
		for foo in skill_payload:
			foo = foo.splitlines()
			for inn in foo:
				college = get_college(inn)
	
				if college is not None:
					isCollegeValid, mycollege = validate_college(college, req2, n)
					resume_data["college"] = mycollege
					if(isCollegeValid):
						return True

	if(check_college(skill_payload)):
		points += 1

	if skillFound is not None:
		if skillFound == True:
			points += 1

	resume_json = json.dumps(resume_data, ensure_ascii=False)
	# print(resume_json)
	r.set("resume" + n, resume_json)
	
	print("resume" + n + " : " + "Points : " + str(points) + "/3")
	location = subprocess.check_output("pwd", shell=True).decode("utf-8")

	if(points >= 2):
		return True, (location[:-1] + filename[1:])
	else:
		return False, (location[:-1] + filename[1:])