from src.extract import scrape_pdf
from src.utils import get_cgpa, get_college, get_skills

import spacy
from nltk.tokenize import sent_tokenize

# helper functions for validating various criteria

def validate_cgpa(cgpa, requirement):

	if(float(cgpa) >= float(requirement)):
		return True

def validate_college(college, requirement):

	f = open("./data/college_dataset/" + requirement, 'r')
	college_dataset = f.read().lower().replace(',', '').split()

	college = college.replace(',', '').replace('.', '').replace('–', '').replace('-', '').replace('(', '').replace(')', '').split()
	if(set(college).issubset(college_dataset) and len(college) >= 2):
		return True

def validate_skills(skills, requirement):

	if(requirement in skills.replace(',', '').replace('.', '').split()):
		return True

# determine the resume score

def resume_score(req1, req2, req3):

	item = scrape_pdf("./data/resume_dataset/resume.pdf")
	#sentences = sent_tokenize(extracted)
	
	points = 0
	
	#for item in sentences:
	cgpa = get_cgpa(item)
	college = get_college(item)
	skills = get_skills(item, req3)

	if cgpa is not None:
		if(validate_cgpa(cgpa, req1)):
			print(cgpa)
			points += 1

	'''if college is not None:
		if(validate_college(college, req2)):
			print(college)
			points += 1'''

	if skills is not None:
		if skills == True:
			points += 1
	
	print("Points : " + str(points) + "/3")