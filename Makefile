install:
	pip3 install -r requirements.txt
	python3 -m spacy download en

go:
	redis-server
	python3 app.py