import spacy

import re
NoneType = type(None)

def get_cgpa(text):
	for token in text:
		if str(token) in ['CGPA', 'GPA', 'CPI', '10', 'out of', '5.0', '10.0', '/10']:
			myset = [text[i] for i in range(token.i - 5, token.i + 5)]
			gpa = list(filter(lambda x: x.like_num == True, myset))
			try:
				gpa = (str((gpa[0])).split('/', 1)[0])
				if('.' in gpa):
					return gpa
			except IndexError:
				print("", end='')
				return 0
	

def get_college(text):
	text = text.lower().replace(',', '').replace('.', '').replace('–', '').replace('-', '').replace('(', '').replace(')', '')

	college_regex = re.compile(r"(.*)(bachelor|education|college|university|institute|engineering|technology)(.*)")
	college_string = college_regex.search(text)

	if not isinstance(college_string, NoneType):
		college_string = college_string.group(0)
	else:
		return

	return college_string

def get_skills(text, n):

	skill = str([sent for sent in text.sents if 'skill' or 'languages' or 'interest' or 'software' or 'platform' or 'programming' or 'tool' or 'framework' in sent.string.lower()]).replace(',', '').splitlines()
	return skill