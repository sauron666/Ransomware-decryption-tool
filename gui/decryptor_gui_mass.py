
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import platform
from tkinter.scrolledtext import ScrolledText

# Dummy decryptor logic
def run_decryption_recursive(paths, dest_path, ransomware_type, key, log_widget):
    for root_path in paths:
        for subdir, dirs, files in os.walk(root_path):
            for file in files:
                full_path = os.path.join(subdir, file)
                try:
                    log_widget.insert(tk.END, f"Decrypting: {full_path}\n")
                    # Placeholder decrypt logic
                    # Replace with actual decryptor logic
                    # Example: decrypt_file(full_path, dest_path, ransomware_type, key)
                except Exception as e:
                    log_widget.insert(tk.END, f"Failed: {full_path} - {str(e)}\n")
    log_widget.insert(tk.END, "Decryption finished.\n")

def list_devices():
    drives = []
    system = platform.system()
    if system == "Windows":
        import string
        from ctypes import windll
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(f"{letter}:/")
            bitmask >>= 1
    elif system in ("Linux", "Darwin"):
        mounts = os.popen("mount | grep '^/dev/'").read().splitlines()
        for line in mounts:
            parts = line.split()
            if len(parts) > 2:
                drives.append(parts[2])
    return drives

# GUI Setup
root = tk.Tk()
root.title("Universal Ransomware Decryptor")
root.geometry("700x500")

tk.Label(root, text="Destination Folder:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
dest_entry = tk.Entry(root, width=60)
dest_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: dest_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2)

tk.Label(root, text="Ransomware Type:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
ransomware_types = ["xor_demo", "stop_djvu", "gandcrab", "custom"]
ransomware_combo = ttk.Combobox(root, values=ransomware_types, state="readonly", width=57)
ransomware_combo.current(0)
ransomware_combo.grid(row=1, column=1, padx=5)

tk.Label(root, text="Decryption Key:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
key_entry = tk.Entry(root, width=60)
key_entry.grid(row=2, column=1, padx=5)

tk.Label(root, text="Select Drives to Decrypt:").grid(row=3, column=0, sticky="nw", padx=10, pady=5)
drive_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=6, width=60)
for d in list_devices():
    drive_listbox.insert(tk.END, d)
drive_listbox.grid(row=3, column=1, padx=5, pady=5)

log_output = ScrolledText(root, height=10, width=80)
log_output.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

def start_mass_decryption():
    selected_indices = drive_listbox.curselection()
    selected_drives = [drive_listbox.get(i) for i in selected_indices]
    dest_path = dest_entry.get()
    ransomware_type = ransomware_combo.get()
    key = key_entry.get()
    if not selected_drives:
        messagebox.showwarning("Warning", "Please select at least one drive.")
        return
    if not dest_path or not key:
        messagebox.showwarning("Warning", "Please enter destination and decryption key.")
        return
    log_output.insert(tk.END, f"Starting decryption for: {', '.join(selected_drives)}\n")
    run_decryption_recursive(selected_drives, dest_path, ransomware_type, key, log_output)

tk.Button(root, text="Start Mass Decryption", command=start_mass_decryption, bg="#4CAF50", fg="white", height=2).grid(row=4, column=1, pady=10)

root.mainloop()
