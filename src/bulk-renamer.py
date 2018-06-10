import os
'''
counter = 1
for file in os.listdir("."):
	if file.endswith(".pdf"):
		os.rename(file, "resume" + str(counter) + ".pdf")
		counter += 1
'''
f=open('../data/pstatus','r')
processed=f.read()
print(processed)

files=os.listdir('../data/resume_dataset/')
print(files)
print(len(files))

processed=int(processed)

counter=processed+1
src='../data/resume_dataset/'
for f in os.listdir('../data/resume_dataset/'):
    
    if f.endswith(".pdf"):
        if(f.find("resume")==-1):
            print(f)
            os.rename(src+f,src+ "resume" + str(counter) + ".pdf")
            counter=counter+1
    
    elif f.endswith(".docx"):
        if(f.find("resume")==-1):
            print(f)
            os.rename(src+f,src+ "resume" + str(counter) + ".docx")
            counter=counter+1
            
    
    
    
            
            
            