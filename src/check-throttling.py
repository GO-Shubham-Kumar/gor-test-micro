import requests
import json
from datetime import datetime
from threading import Thread

def check_throttling(index = 0):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[Thread {index}] URL Req Made at : ", current_time)

    url = "http://go-throtting-test.us-e2.cloudhub.io/"
    headers = {"client_id": "10d493f8745b42cc808861f25a29bcbd", "client_secret": "90aF65EE3a93414880fE5c6cA24bc272"}
    response_API = requests.get(url, headers=headers)
    print(response_API.json())

t = []
for i in range(1, 3):
    t.append(Thread(target=check_throttling, args = (i,), daemon=True))
    t[-1].start()

for _ in t:
    _.join()
