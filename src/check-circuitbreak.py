import requests
import json
from datetime import datetime
from threading import Thread

words = ["", "nword", "nword", "nword", "goodword", "perfect"]

def check_throttling(word = ""):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[LOOP {word}] URL Req Made at : ", current_time)

    url = f"http://go-greetings-test.us-e2.cloudhub.io/greetings?name={word}"
    response_API = requests.get(url)
    print(response_API.json())

t = []
for word in words:
    # t.append(Thread(target=check_throttling, args = (i,), daemon=True))
    #t[-1].start()
    check_throttling(word)

