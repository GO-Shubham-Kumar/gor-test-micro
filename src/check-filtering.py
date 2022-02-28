import requests
import json
from datetime import datetime
from threading import Thread

def check_throttling(index = 0):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[Thread {index}] URL Req Made at : ", current_time)

    url = "http://go-policy-test.us-e2.cloudhub.io/"
    response_API = requests.get(url)
    print(response_API.json())

t = []
for i in range(1, 6):
    t.append(Thread(target=check_throttling, args = (i,), daemon=True))
    t[-1].start()

for _ in t:
    _.join()
