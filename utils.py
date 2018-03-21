import re
NoneType = type(None)

def get_cgpa(text):
	text = text.lower()

	gpa_regex = re.compile(r"gpa|cpi(.*)[0-9].[0-9](.*)/(.*)10")
	cgpa_string = gpa_regex.search(text)

	if not isinstance(cgpa_string, NoneType):
		cgpa_string = cgpa_string.group(0)
	else:
		return

	num_regex = re.compile(r"[+-]?\d+(?:\.\d+)?")
	cgpa = num_regex.search(cgpa_string)

	if not isinstance(cgpa, NoneType):
		cgpa = cgpa.group(0)
	else:
		return

	return cgpa

def get_college(text):
	text = text.lower()

	college_regex = re.compile(r"(.*)(education|college|university|institute|engineering)(.*)")
	college_string = college_regex.search(text)

	if not isinstance(college_string, NoneType):
		college_string = college_string.group(0)
	else:
		return

	return college_string

def get_skills(text):
	text = text.lower()

	skills_regex = re.compile(r"(skill|interest|language|area|programming|tool|framwork|coding|platform|software|os|extensive|expert|intermediate|beginner|basic)(.*)(\D*)[^*]")
	skills_string = skills_regex.search(text)

	if not isinstance(skills_string, NoneType):
		skills_string = skills_string.group(0)
	else:
		return

	return skills_string