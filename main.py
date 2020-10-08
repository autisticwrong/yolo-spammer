import random
import requests
import string
from time import sleep
import sys

BASE_URL = "https://onyolo.com/"

# Find your user agent in https://www.whatismybrowser.com/detect/what-is-my-user-agent

HEADERS = {
  "user-agent": "Enter your user agent here"
}

DATA = {
  "text": "",
  "cookie": "",
  "wording": ""
}

user_id = input("Enter a YOLO ID: ")

response = requests.get(f"http://onyolo.com/m/{user_id}", headers=HEADERS)
if response.content == b"Not Found":
  print("The YOLO ID does not exist")
  sys.exit()

DATA["text"] = input("Enter a message: ")
DATA["cookie"] = "".join(random.choices(string.ascii_lowercase + string.digits, k=22))

BASE_URL = BASE_URL + user_id + "/message"

count = 1

# Your user agent might get banned so set a rate limit
for i in range(50):
  DATA["wording"] = f"#{count}"
  response = requests.post(BASE_URL, json=DATA, headers=HEADERS)
  print(f"Sent #{count}")
  count += 1
  sleep(0.03125)
