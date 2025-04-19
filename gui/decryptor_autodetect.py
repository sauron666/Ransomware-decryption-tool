
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from collections import defaultdict
from tkinter.scrolledtext import ScrolledText

# Known ransomware extensions and mappings
RANSOMWARE_SIGNATURES = {
    ".hush": "Hush / MoneyIsTime",
    ".djvu": "STOP Djvu",
    ".gandcrab": "GandCrab",
    ".locked": "Generic Ransomware",
    ".krab": "GandCrab",
    ".lol": "Jigsaw",
    ".enc": "Generic",
    ".encrypted": "Generic"
}

def scan_for_encrypted_files(scan_path, log_widget):
    found = defaultdict(list)
    for root, dirs, files in os.walk(scan_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in RANSOMWARE_SIGNATURES:
                full_path = os.path.join(root, file)
                found[ext].append(full_path)
    for ext, paths in found.items():
        log_widget.insert(tk.END, f"Detected extension '{ext}' ({RANSOMWARE_SIGNATURES[ext]}):\n")
        for p in paths:
            log_widget.insert(tk.END, f"  {p}\n")
    if not found:
        log_widget.insert(tk.END, "No known ransomware extensions found.\n")
    return found

def suggest_ransomware_type(found):
    if not found:
        return "unknown"
    # Prioritize based on occurrence
    most_common = max(found.items(), key=lambda item: len(item[1]))
    ext = most_common[0]
    return RANSOMWARE_SIGNATURES.get(ext, "unknown")

# GUI setup
root = tk.Tk()
root.title("Auto-Detect Ransomware Scanner")
root.geometry("750x480")

tk.Label(root, text="Select Folder or Drive to Scan:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
scan_entry = tk.Entry(root, width=70)
scan_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: scan_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2)

log_output = ScrolledText(root, height=20, width=90)
log_output.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

def start_scan():
    scan_path = scan_entry.get()
    if not scan_path or not os.path.exists(scan_path):
        messagebox.showwarning("Warning", "Please select a valid folder or drive.")
        return
    log_output.insert(tk.END, f"Scanning: {scan_path}\n")
    found = scan_for_encrypted_files(scan_path, log_output)
    suggestion = suggest_ransomware_type(found)
    if suggestion != "unknown":
        log_output.insert(tk.END, f"\nSuggested ransomware type: {suggestion}\n")
    else:
        log_output.insert(tk.END, "\nCould not identify ransomware type.\n")

tk.Button(root, text="Start Auto-Detect", bg="#2196F3", fg="white", height=2, command=start_scan).grid(row=1, column=1, pady=10)

root.mainloop()
