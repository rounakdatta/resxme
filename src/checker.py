import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

import json
from decimal import Decimal

n = 20

for i in range(1, n+1):
	curr_resume = "resume" + str(i)
	payload = json.loads(r.get(curr_resume).decode('utf8').replace("'", '"'))
	print(str(i) + " " + payload["college"])