import json, requests, sys, time, webbrowser, stat
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from tkinter import ttk
import subprocess, os, shutil, string, threading, win32api, serial, serial.tools.list_ports
from playsound import playsound

# VARIABLEN
github_repo="https://github.com/flogreth/Frisbee/tree/main/software/default_codes/frisbee_2_pi_pico_neopixel_default"
circuitpython_list = "https://raw.githubusercontent.com/thonny/thonny/master/data/circuitpython-variants-uf2.json"
circuitpython_link = "https://downloads.circuitpython.org/bin/raspberry_pi_pico_w/en_US/adafruit-circuitpython-raspberry_pi_pico_w-en_US-9.2.8.uf2"

letzter_versuch = 0
versuche = 0
repo_url = ""
subfolder = ""

# circuitpython Versions-Liste holen
data = requests.get(circuitpython_list).json()
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

def parse_github_url(url):
    global subfolder, repo_url
    """Wandelt einen GitHub-Browser-Link in Repo-URL + Subfolder um"""
    if "/tree/" not in url:
        raise ValueError("URL muss '/tree/' enthalten")
    parts = url.split("/tree/")
    repo_url = parts[0] + ".git"
    after_tree = parts[1].split("/", 1)
    if len(after_tree) < 2:
        raise ValueError("Kein Subfolder in der URL gefunden")
    subfolder = after_tree[1]
    return repo_url, subfolder

def delete_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory, onerror=handle_remove_readonly)

def handle_remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def start_toast_thread():
    empty_log()
    log("let the toasting begin")
    
    threading.Thread(target=start_toast, daemon=True).start()

def start_toast():

    tmp_dir = "tmp_clone"
    delete_dir(tmp_dir)

    # CircuitPython-Ziel finden
    cpy_ziel = find_device("RPI-RP2")
    if not cpy_ziel:
        log("Device 'RPI-RP2' nicht gefunden. Bootloader-Button gedrückt!?")
        return

    # CircuitPython herunterladen
    
    dateiname = os.path.join(cpy_ziel, os.path.basename(circuitpython_link))
    response = requests.get(circuitpython_link, stream=True)
    log(f"Downloading CircuitPython file...{dateiname}")
    with open(dateiname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    log("...finished")
    log("Restarting microcontroller...")

    parse_github_url(github_repo)

    max_versuche = 5
    versuche = 0
    while versuche < max_versuche:
        ziel = find_device("CIRCUITPY")
        if ziel:
            log("Device 'CIRCUITPY' gefunden!")
            
            # Zielordner leeren
            log("Alle Dateien löschen...")
            for item in os.listdir(ziel):
                pfad = os.path.join(ziel, item)
                try:
                    if os.path.isfile(pfad) or os.path.islink(pfad):
                        os.unlink(pfad)
                    else:
                        shutil.rmtree(pfad)
                except Exception as e:
                    log(f"Fehler beim Löschen: {e}")

            # Repo klonen
            log(f"Cloning {repo_url}, folder: {subfolder}")
            subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", repo_url, tmp_dir])
            subprocess.run(["git", "-C", tmp_dir, "sparse-checkout", "set", subfolder])

            full_subfolder = os.path.join(tmp_dir, subfolder)
            if not os.path.exists(full_subfolder):
                log(f"Fehler: Subfolder '{subfolder}' existiert nicht im geklonten Repo!")
                shutil.rmtree(tmp_dir, ignore_errors=True)
                return

            # Dateien kopieren
            all_files = [os.path.join(r, f) for r, _, fs in os.walk(full_subfolder) for f in fs]
            total = len(all_files)

            for i, src in enumerate(all_files, 1):
                dst = os.path.join(ziel, os.path.relpath(src, full_subfolder))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                log(f"{i}/{total} {os.path.basename(src)}")
            shutil.rmtree(tmp_dir, ignore_errors=True)

            log("Sucessfully toasted!")

            playsound("media/finished.mp3")
            
            delete_dir(tmp_dir)
            break
        else:
            versuche += 1
            log(".")
            time.sleep(2)
    else:
        log("Nicht gefunden nach 5 Versuchen.")



def log(text):
    log_box.insert(tk.END, text + "\n")
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
                    log("circuitpython downloadlink gefunden:")
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
root.geometry("680x600")
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
url_entry = tk.Entry(root, width=80, justify="left")
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

