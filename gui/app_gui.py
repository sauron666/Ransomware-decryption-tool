
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from decryptors import xor_demo  # Expand with more modules
from main import decrypt_file

def browse_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

def browse_destination():
    folderpath = filedialog.askdirectory()
    if folderpath:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folderpath)

def start_decryption():
    file_path = file_entry.get()
    destination_path = destination_entry.get()
    ransomware_type = ransomware_type_var.get()
    key = key_entry.get()

    if not file_path or not destination_path or not key:
        messagebox.showerror("Missing Info", "Please fill in all fields.")
        return

    try:
        key_value = int(key, 0)  # Accepts hex (0x...), decimal, etc.
        decrypt_file(file_path, destination_path, ransomware_type, key_value)
        messagebox.showinfo("Success", "Decryption complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = tk.Tk()
root.title("Universal Ransomware Decryptor")
root.geometry("500x300")

tk.Label(root, text="Encrypted File:").pack(pady=5)
file_entry = tk.Entry(root, width=60)
file_entry.pack()
tk.Button(root, text="Browse", command=browse_file).pack()

tk.Label(root, text="Destination Folder:").pack(pady=5)
destination_entry = tk.Entry(root, width=60)
destination_entry.pack()
tk.Button(root, text="Browse", command=browse_destination).pack()

tk.Label(root, text="Ransomware Type:").pack(pady=5)
ransomware_type_var = tk.StringVar()
ransomware_type_dropdown = ttk.Combobox(root, textvariable=ransomware_type_var)
ransomware_type_dropdown['values'] = ('xor_demo',)  # Expand as you add more
ransomware_type_dropdown.current(0)
ransomware_type_dropdown.pack()

tk.Label(root, text="Decryption Key:").pack(pady=5)
key_entry = tk.Entry(root, width=30)
key_entry.pack()

tk.Button(root, text="Start Decryption", command=start_decryption, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
