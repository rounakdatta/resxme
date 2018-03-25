from extract import scrape_pdf
from utils import get_cgpa, get_college, get_skills

from nltk.tokenize import sent_tokenize

# helper functions for validating various criteria

def validate_cgpa(cgpa, requirement):

	if(float(cgpa) >= float(requirement)):
		return True

def validate_college(college, requirement):

	f = open(requirement, 'r')
	college_dataset = f.read().lower().replace(',', '').split()

	college = college.replace(',', '').replace('.', '').replace('–', '').replace('-', '').replace('(', '').replace(')', '').split()
	if(set(college).issubset(college_dataset) and len(college) >= 2):
		return True

def validate_skills(skills, requirement):

	if(requirement in skills.replace(',', '').replace('.', '').split()):
		return True

# determine the resume score

def resume_score():

	extracted = scrape_pdf("resume.pdf")
	sentences = sent_tokenize(extracted)
	
	points = 0
	
	for item in sentences:
		cgpa = get_cgpa(item)
		college = get_college(item)
		skills = get_skills(item)
	
		if cgpa is not None:
			if(validate_cgpa(cgpa, 7.5)):
				print(cgpa)
				points += 1
	
		if college is not None:
			if(validate_college(college, "T1")):
				print(college)
				points += 1
	
		if skills is not None:
			if(validate_skills(skills, "c++")):
				print(skills)
				points += 1
	
	print("Points : " + str(points) + "/3")


resume_score()