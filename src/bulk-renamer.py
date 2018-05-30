import os

counter = 1
for file in os.listdir("."):
	if file.endswith(".pdf"):
		os.rename(file, "resume" + str(counter) + ".pdf")
		counter += 1