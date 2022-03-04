import requests
import json
from datetime import datetime
from threading import Thread

def check_throttling(index = 0):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[LOOP {index}] URL Req Made at : ", current_time)

    url = "http://go-greetings-test.us-e2.cloudhub.io/greetings?name=nword"
    response_API = requests.get(url)
    print(response_API.json())

t = []
for i in range(1, 11):
    # t.append(Thread(target=check_throttling, args = (i,), daemon=True))
    #t[-1].start()
    check_throttling(i)

