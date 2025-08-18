# to make an executable file type:
# python -m PyInstaller --onefile --noconsole Frisbee-toaster_v03.py

import json, requests, sys, time, webbrowser, stat
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from tkinter import ttk
import subprocess, os, shutil, string, threading, win32api, serial, serial.tools.list_ports
from playsound import playsound
from pathlib import Path
from urllib.parse import urlparse
from secrets import GITHUB_TOKEN


# VARIABLEN
github_repo="https://github.com/flogreth/Frisbee/tree/main/software/default_codes/frisbee_3_pi_pico_w"
circuitpython_list = "https://raw.githubusercontent.com/thonny/thonny/master/data/circuitpython-variants-uf2.json"
circuitpython_link = "https://downloads.circuitpython.org/bin/raspberry_pi_pico_w/en_US/adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.2.8.uf2"
headers = {"Authorization": f"token {GITHUB_TOKEN}"} #from separate secrets file

letzter_versuch = 0
versuche = 0
repo_url = ""
subfolder = ""

# circuitpython Versions-Liste holen
data = requests.get(circuitpython_list, headers=headers).json()
rp2_entries = [item for item in data if item.get("vendor") == "Raspberry Pi"]


class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
    def write(self, string):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)
    def flush(self):
        pass

def find_device(devicename):
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        try:
            name, _, _, _, _ = win32api.GetVolumeInformation(drive)
            if name == devicename:
                return drive
        except:
            pass
    return None

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

def delete_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory, onerror=handle_remove_readonly)

def handle_remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def start_toast_thread():
    empty_log()
    log("let the toasting begin...")
    
    threading.Thread(target=start_toast, daemon=True).start()

def count_items(api_url):
    r = requests.get(api_url, headers=headers)
    r.raise_for_status()
    items = r.json()
    total = 0
    for item in items:
        if item["type"] == "file":
            total += 1
        elif item["type"] == "dir":
            total += count_items(item["url"])
    return total

def download_github_folder_api(api_url, ziel, total=None, progress=[0]):
    if total is None:
        total = count_items(api_url)
    r = requests.get(api_url, headers=headers)
    r.raise_for_status()
    items = r.json()
    ziel = Path(ziel)
    ziel.mkdir(parents=True, exist_ok=True)
    for item in items:
        if item["type"] == "file":
            file_r = requests.get(item["download_url"], headers=headers)
            progress[0] += 1
            prozent = round((progress[0] / total) * 100, 1)
            log_replace_last(f"copy file {progress[0]} von {total} ({prozent}%) ......{item['name']}")
            with open(ziel/item["name"], "wb") as f:
                f.write(file_r.content)
        elif item["type"] == "dir":
            progress[0] += 1
            prozent = round((progress[0] / total) * 100, 1)
            log_replace_last(f"copy directory {progress[0]} von {total} ({prozent}%) ....{item['name']}")
            download_github_folder_api(item["url"], ziel/item["name"], total=total, progress=progress)


def start_toast():

    toast_button.config(state=tk.DISABLED)
    tmp_dir = "tmp_clone"
    delete_dir(tmp_dir)

    # CircuitPython-Ziel finden
    cpy_ziel = find_device("RPI-RP2")
    if not cpy_ziel:
        log("Device 'RPI-RP2' not found. Did you push the bootloader button!?")
        return

    # CircuitPython herunterladen
    dateiname = os.path.join(cpy_ziel, os.path.basename(circuitpython_link))
    response = requests.get(circuitpython_link, stream=True, headers=headers)
    log(f"Downloading CircuitPython file...{dateiname}")
    with open(dateiname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    log("CIRCUITPYTHON successfully installed...")
    log("Restarting microcontroller...")
    toast_button.config(state=tk.NORMAL)

    max_versuche = 7
    versuche = 0
    while versuche < max_versuche:
        ziel = find_device("CIRCUITPY")
        if ziel:
            # Zielordner leeren
            files = os.listdir(ziel)
            total = len(files)
            for i, item in enumerate(files, start=1):
                pfad = os.path.join(ziel, item)
                try:
                    percent = int((i / total) * 100)
                    log_replace_last(f"deleting old files... {percent}% ({i}/{total})")
                    if os.path.isfile(pfad) or os.path.islink(pfad):
                        os.unlink(pfad)
                    else:
                        shutil.rmtree(pfad)
                except Exception as e:
                    log(f"Error while deleting: {e}")

            
            api_url = github_url_to_api(github_repo)
            # Repo klonen
            log(f"Cloning {api_url}")
            download_github_folder_api(api_url, ziel)

            log("Sucessfully toasted!")

            playsound("media/finished.mp3")
            
            delete_dir(tmp_dir)
            break
        else:
            versuche += 1
            log(".")
            time.sleep(2)
    else:
        log("not found after 7 tries.. I give up )")



def log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)

def log_replace_last(text):
    log_box.delete("end-2l", "end-1l")  # letzte Zeile löschen
    log_box.insert("end-1l", text + "\n")  # neue Zeile einfügen
    log_box.see(tk.END)

def empty_log():
    log_box.delete("1.0", tk.END)

# Update Versions-Dropdown beim Board-Wechsel
def update_versions(event):
    selected_board = board_var.get()
    for item in rp2_entries:
        if item["model"] == selected_board:
            versions = [v["version"] for v in item.get("downloads", [])]
            if versions:
                version_dropdown['values'] = versions
                version_var.set(versions[0])  # ersten Eintrag automatisch wählen
                set_circuitpy_url(None)
            break

# Circuitpython Version Downloadlink abrufen
def set_circuitpy_url(event):
    global circuitpython_link
    selected_board = board_var.get()
    selected_version = version_var.get()
    for item in rp2_entries:
        if item["model"] == selected_board:
            for v in item.get("downloads", []):
                if v["version"] == selected_version:
                    
                    circuitpython_link = v['url']
                    empty_log()
                    log("matching circuitpython UF2 file found:")
                    log(" ")
                    log(circuitpython_link)
                    break

def check_device():
    if find_device("RPI-RP2"):
        if toast_var.get():
            start_toast_thread()
        else:
            toast_button.config(state=tk.NORMAL)
        
    else:
        toast_button.config(state=tk.DISABLED)
    root.after(1000, check_device)  # alle 1 Sekunde prüfen

root = tk.Tk()
root.geometry("800x600")
root.title("Frisbee Toaster 2.0")

# Erste Auswahl: Board
tk.Label(root, text="Board:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
board_var = tk.StringVar()
board_choices = [item["model"] for item in rp2_entries]
board_dropdown = ttk.Combobox(root, textvariable=board_var, values=board_choices)
board_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Zweite Auswahl: Version
tk.Label(root, text="Version:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
version_var = tk.StringVar()
version_dropdown = ttk.Combobox(root, textvariable=version_var)
version_dropdown.grid(row=1, column=1, padx=5, pady=5)

board_dropdown.bind("<<ComboboxSelected>>", update_versions)
version_dropdown.bind("<<ComboboxSelected>>", set_circuitpy_url)

# GitHub URL
tk.Label(root, text="GitHub-URL:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
url_entry = tk.Entry(root, width=100, justify="left")
url_entry.grid(row=2, column=1, padx=5, pady=5)
url_entry.insert(0, github_repo)

# Öffnen Button
tk.Button(root, text="Öffnen", command=lambda: webbrowser.open(url_entry.get())).grid(
    row=2, column=2, padx=2, pady=5, sticky="e")


# Toast Button
toast_button = tk.Button(root, text="Toast", command=start_toast_thread, width=20)
toast_button.grid(row=3, column=0, columnspan=3, pady=5)

# Checkbox neben Button
toast_var = tk.BooleanVar(value=False)
toast_checkbox = tk.Checkbutton(root, text="Autotoast", variable=toast_var)
toast_checkbox.grid(row=3, column=2, padx=5, pady=5)

# Log Box
log_box = scrolledtext.ScrolledText(root)
log_box.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

#sys.stdout = RedirectText(log_box)
check_device()
if board_choices:
    board_var.set(board_choices[0])  # ersten Boardeintrag wählen
    update_versions(None)  # direkt Versionen setzen

root.mainloop()

