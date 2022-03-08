import requests
import json
from datetime import datetime
from threading import Thread
from time import sleep

words = ["Guru", "nword", "nword", "nword", "goodword", "perfect"]

def check_circuitbreaker(word = ""):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[LOOP {word}] URL Req Made at : ", current_time)

    url = f"http://go-greetings-test.us-e2.cloudhub.io/greetings?name={word}"
    response_API = requests.get(url)
    print(response_API.json())
    print()

t = []
for word in words:

    check_circuitbreaker(word)

t = 10
sleep(t)
print(f"Retry after {t} seconds")
check_circuitbreaker("Shubham")

