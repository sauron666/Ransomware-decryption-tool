
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import platform

# Dummy decryptor function for now
def run_decryption(file_path, dest_path, ransomware_type, key):
    # This would be replaced with actual logic later
    print(f"Decrypting: {file_path}\nTo: {dest_path}\nType: {ransomware_type}\nKey: {key}")
    messagebox.showinfo("Decryption", f"Decryption completed for:\n{file_path}")

def browse_file(entry_widget):
    path = filedialog.askopenfilename()
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)

def browse_folder(entry_widget):
    path = filedialog.askdirectory()
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)

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
root.geometry("600x400")

tk.Label(root, text="Encrypted File:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: browse_file(file_entry)).grid(row=0, column=2, padx=5)

tk.Label(root, text="Destination Folder:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: browse_folder(dest_entry)).grid(row=1, column=2, padx=5)

tk.Label(root, text="Ransomware Type:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
ransomware_types = ["xor_demo", "stop_djvu", "gandcrab", "custom"]
ransomware_combo = ttk.Combobox(root, values=ransomware_types, state="readonly")
ransomware_combo.current(0)
ransomware_combo.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Decryption Key:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=3, column=1, padx=5)

tk.Label(root, text="Target Drive (optional):").grid(row=4, column=0, sticky="w", padx=10, pady=5)
drive_combo = ttk.Combobox(root, values=list_devices(), state="readonly", width=47)
drive_combo.grid(row=4, column=1, padx=5, pady=5)

def start_decryption():
    file_path = file_entry.get()
    dest_path = dest_entry.get()
    ransomware_type = ransomware_combo.get()
    key = key_entry.get()
    run_decryption(file_path, dest_path, ransomware_type, key)

tk.Button(root, text="Start Decryption", command=start_decryption, bg="#4CAF50", fg="white", height=2).grid(row=5, column=1, pady=20)

root.mainloop()
