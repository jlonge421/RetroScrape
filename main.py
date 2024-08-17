import requests
import os

url = "ltgcoaches.com"
timeout = 15
dir_name = "WayBack Archives"

def fetch_snapshots(url, timeout):
    try:
        wb_api_url = "https://web.archive.org/cdx/search/cdx"
        params = {
            "url": url,
            "output": "json",
            "filter": "statuscode:200",
            "fl":"original, timestamp"
        }
        response = requests.get(wb_api_url, params=params, timeout=timeout)
        print(response.status_code)
        print(response.json())
    except requests.exceptions.Timeout:
        print("Timeout! 15 Seconds!! Think about your actions...")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def pull_snapshot(url, timestamp, dir_name):
    archive_url = f"https://web.archive.org/web/{timestamp}/{url}"
    try:
        response = requests.get(archive_url)
        response.raise_for_status()

        shaved_url = url.replace("https://", "").replace("/", "_")
        filename = f"{timestamp}_{shaved_url}.html"
        filepath = os.path.join(dir_name, filename)

        with open(filepath, "W", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Whoopsy Poopsy, I couldn't retrieve {archive_url}: {e}")

def processor(url, dir_name, timeout):
    os.makedirs(dir_name, exists_ok=True)
    snapshots = fetch_snapshots(url, timeout)
    if snapshots:
        for snapshot in snapshots:
            timestamp, url = snapshot
            pull_snapshot(url, timestamp, dir_name)
        else:
            print("No snapshots here.. :(   \nidk try again maybe?")
