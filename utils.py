import re

def get_cgpa(text):
	text = text.lower()

	gpa_regex = re.compile(r"gpa(.*)[0-9].[0-9](.*)/(.*)10")
	cgpa_string = gpa_regex.search(text).group(0)

	regex = re.compile(r"[+-]?\d+(?:\.\d+)?")
	cgpa = num_regex.search(cgpa_string).group(0)
	return cgpa

def get_college(text):
	text = text.lower()

	college_regex = re.compile(r"education|college|university|institute(.*)[a-zA-Z0-9]")
	college_string = college_regex.search(text).group(0)

	return college_string