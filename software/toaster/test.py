import requests
from pathlib import Path
from urllib.parse import urlparse

def github_url_to_api(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if "tree" in parts:
        tree_idx = parts.index("tree")
        repo = "/".join(parts[:2])
        branch = parts[tree_idx + 1]
        folder_path = "/".join(parts[tree_idx + 2:])
        api_url = f"https://api.github.com/repos/{repo}/contents/{folder_path}?ref={branch}"
        return api_url
    else:
        raise ValueError("URL muss /tree/ enthalten.")

def download_github_folder_api(api_url, ziel):
    headers = {"Authorization": "token DEIN_TOKEN"}
    r = requests.get(api_url, headers=headers)
    r.raise_for_status()
    ziel.mkdir(parents=True, exist_ok=True)

    for item in r.json():
        if item["type"] == "file":
            file_r = requests.get(item["download_url"])
            with open(ziel/item["name"], "wb") as f:
                f.write(file_r.content)
        elif item["type"] == "dir":
            # rekursiv Unterordner laden
            sub_api_url = f"https://api.github.com/repos/{item['url'].split('/repos/')[1]}"
            download_github_folder_api(item["url"], ziel/item["name"])

# Nutzung:
github_url = "https://github.com/flogreth/Frisbee/tree/main/software/default_codes/frisbee_2_pi_pico_neopixel_default"
ziel = Path("zielordner")

api_url = github_url_to_api(github_url)
download_github_folder_api(api_url, ziel)
