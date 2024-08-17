import requests

response = requests.get("http://web.archive.org/cdx/search/cdx?url=ltgcoaches.com&output=json")
print(response.json())