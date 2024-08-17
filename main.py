import requests
import os

response = requests.get("https://dog.ceo/api/breeds/list/all", timeout=10)
print(response.status_code)
print(response.json())
print("hello")
exit()