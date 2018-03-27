import spacy

import re
NoneType = type(None)

def get_cgpa(text):
	for token in text:
		if str(token) in ['CGPA', 'GPA', 'CPI']:
			myset = [text[i] for i in range(token.i - 5, token.i + 5)]
			gpa = list(filter(lambda x: x.like_num == True, myset))
			gpa = (str((gpa[0])).split('/', 1)[0])

			return gpa

def get_college(text):
	'''text = text.lower()

	college_regex = re.compile(r"(.*)(education|college|university|institute|engineering)(.*)")
	college_string = college_regex.search(text)

	if not isinstance(college_string, NoneType):
		college_string = college_string.group(0)
	else:
		return

	return college_string'''
	return 0

def get_skills(text, query):

	skill = str([sent for sent in text.sents if 'skill' or 'languages' or 'interest' or 'software' or 'platform' or 'programming' or 'tool' or 'framework' in sent.string.lower()]).replace(',', '').splitlines()

	for el in skill:
		if query in str(el).lower():
			return True

	return False