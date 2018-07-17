
# ResXme - The Resume Mining Tool

ResXme is a resume parsing tool that can read resumes in PDFs, DocX formats. Once resumes are submitted each resume can be evaluated based on queries if certain parameters match / not. The tool makes resume search (mining for criteria) super-easy and fast.

## NLP

The project makes extensive use of the following Python NLP libraries:
 - **SpaCy** (excellent library for identifying sentences, tokenizing sentence)
 - **NLTK** (helps in tokenizing)
- **Regex** (used to find out useful patterns in data)

## Algorithms

Consists of three sub-sections - CGPA, college, skills and has **extracting** and **validating** tools for each of them.

- [bulk-renamer.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/bulk-renamer.py) - to rename the resumes in an order (not required if each one's unique)
- [extract.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/extract.py) - to scrape data from a PDF-format resume (uses pdfminer).
- [extract1.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/extract1.py) - to scrape data from a DocX-format resume (uses docx2txt)
- [utils.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/utils.py) - contains all the necessary functions for extracting the required criteria from the scraped document.
- [validator.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/validator.py) - contains all the required functions to validate if the extracted criteria matches with the specified data. Also, the resume score is returned (depending on how many matches are found).
- [checker.py](https://github.com/rounakdatta/resxme/blob/webapp-spacy/src/checker.py) - to handle the traversing of resumes

## System Design

![Architecture Diagram](https://i.imgur.com/7olSjVE.png)

## Getting started

The project has been built entirely using Python 3. The backend framework is powered by Flask. To install all the dependencies, you need to clone the repository, navigate to it and type ``make install``. To start the application, you can type ``make go`` OR ``python3 app.py`` and then navigate to [localhost:5000](http://localhost:5000).

The application can be used by inputting the criteria (threshold **CGPA**, T1 **college**/not, required **skills**). As output, JSON is returned which consists all the resumes that satisfy 2/3 or above of the given criteria.

Following are the attributes of the JSON for each resume displayed:

 - Resume file name
 - Resume location
 - CGPA match (T/F)
 - College match (T/F)
 - Skill found (T/F)
 - Total score (out of 3)
