import requests
from urllib.parse import quote


def fetch_scripture(reference):
    safe_reference = quote(reference)
    url = f"https://bible-api.com/{safe_reference}"

    try:
        r = requests.get(url, timeout=10)
    except requests.RequestException:
        return None

    if r.status_code != 200:
        return None

    data = r.json()
    return data.get("text", None)