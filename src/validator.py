from src.extract import scrape_pdf
from src.extract1 import scrape_docx
from src.utils import get_cgpa, get_college, get_skills

import spacy
from nltk.tokenize import sent_tokenize
import subprocess

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

import json
from decimal import Decimal

# helper functions for validating various criteria

def find_college(college, n):

    f = open("./data/college_dataset/T1", 'r')
    college_dataset = f.read().lower().replace(',', '').splitlines()

    college = college.replace(',', '').replace('.', '').replace('–', '').replace('-', '').replace('(', '').replace(')', '')

    for single_college in college_dataset:
        if(single_college in college):
            return single_college

    return "null"

# determine the resume score

def resume_score(n):

    filename = "./data/resume_dataset/resume" + n + ".pdf"
    itemx = scrape_pdf(filename)
    nlp = spacy.load('en_core_web_sm')
    item = nlp(itemx)

    skill_payload = sent_tokenize(itemx)
    
    resume_data = {}
    
    cgpa = get_cgpa(item)
    resume_data["cgpa"] = cgpa

    skills = get_skills(item, n)
    resume_data["skills"] = skills

    def skill_calc():
        for foo in skill_payload:
            foo = foo.splitlines()
            for inn in foo:
                college = get_college(inn)
    
                if college is not None:
                    mycollege = find_college(college, n)
                    if(mycollege != "null"):
                        resume_data["college"] = mycollege
                        return True
    if(not skill_calc()):
        resume_data["college"] = "null"

    resume_json = json.dumps(resume_data, ensure_ascii=False)
    r.set("resume" + n, resume_json)

def resume_score1(n):
    #print("rs1",n)
    filename = "./data/resume_dataset/resume" + n + ".docx"
    itemx = scrape_docx(filename)
    nlp = spacy.load('en_core_web_sm')
    item = nlp(itemx)
    print("item")
    skill_payload = sent_tokenize(itemx)
    
    resume_data = {}
    
    cgpa = get_cgpa(item)
    resume_data["cgpa"] = cgpa

    skills = get_skills(item, n)
    resume_data["skills"] = skills

    def skill_calc():
        for foo in skill_payload:
            foo = foo.splitlines()
            for inn in foo:
                college = get_college(inn)
    
                if college is not None:
                    mycollege = find_college(college, n)
                    if(mycollege != "null"):
                        resume_data["college"] = mycollege
                        return True
    if(not skill_calc()):
        resume_data["college"] = "null"

    resume_json = json.dumps(resume_data, ensure_ascii=False)
    r.set("resume" + n, resume_json) 
