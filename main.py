import requests
import os
try:
    response = requests.get("https://web.archive.org/cdx/search/cdx?url=ltgcoaches.com", timeout=10)
    print(response.status_code)
    print(response.json())
 except requests.exceptions.Timeout:
        print("Timeout! Think about your actions...")
print("hello")
