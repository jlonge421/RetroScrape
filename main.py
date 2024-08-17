import requests
import os


try:
    wb_api_url = "https://web.archive.org/cdx/search/cdx"
    params = {
        "url": "ltgcoaches.com",
        "output": "json",
        "filter": "statuscode:200",
        "fl":"original, timestamp"
    }
    response = requests.get(wb_api_url, params=params, timeout = 15)
    print(response.status_code)
    print(response.json())
except requests.exceptions.Timeout:
    print("Timeout! Think about your actions...")
print("hello")
