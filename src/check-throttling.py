import requests
import json
from datetime import datetime
from threading import Thread

def check_throttling(index = 0):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"[Thread {index}] URL Req Made at : ", current_time)

    url = "http://go-throtting-test.us-e2.cloudhub.io/"
    response_API = requests.get(url)
    print(response_API.json())


t_1 = Thread(target=check_throttling, args = (1,))
t_2 = Thread(target=check_throttling, args = (2,))

t_1.start()
t_2.start()
t_1.join()
t_2.join()
