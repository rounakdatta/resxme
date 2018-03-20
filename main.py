from extract import scrape_pdf
from utils import get_cgpa, get_college, get_skills

from nltk.tokenize import sent_tokenize

extracted = scrape_pdf("resume.pdf")

sentences = sent_tokenize(extracted)

for item in sentences:
	cgpa = get_cgpa(item)
	college = get_college(item)
	skills = get_skills(item)

	if cgpa is not None:
		print(cgpa)
	if college is not None:
		print(college)
	if skills is not None:
		print(skills)