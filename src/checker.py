import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

import json
from decimal import Decimal

n = 44
good_results = 0

for i in range(1, n+1):
	curr_resume = "resume" + str(i)
	try:
		payload = json.loads(r.get(curr_resume).decode('utf8').replace("'", '"'))
		print(payload["cgpa"])
		good_results += 1
	except:
		print("null")

print(str(good_results) + " good results")