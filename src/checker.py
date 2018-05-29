import pyrebase

config = {
  "apiKey": "AIzaSyB8AHvyWEhrs5H-iE3CCMa0J5LRDyVHqsg",
  "authDomain": "resxme-6c10f.firebaseapp.com",
  "databaseURL": "https://resxme-6c10f.firebaseio.com",
  "storageBucket": "resxme-6c10f.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

for i in range(1, 16):
	curr_file = "resume" + str(i)
	cgpa = db.child("candidates").child(curr_file).child("cgpa").get()
	college = db.child("candidates").child(curr_file).child("college").get()
	skills = db.child("candidates").child(curr_file).child("skills").get()
	print(cgpa.val())
	print(college.val())