
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

CONFIG_FILE = "universal_decryptor/config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def refresh_list():
    config = load_config()
    listbox.delete(0, tk.END)
    for k in config:
        listbox.insert(tk.END, k)

def on_select(event):
    config = load_config()
    selection = listbox.curselection()
    if not selection:
        return
    key = listbox.get(selection[0])
    item = config[key]
    name_var.set(key)
    desc_var.set(item.get("description", ""))
    module_var.set(item.get("module", ""))
    key_type_var.set(item.get("key_type", ""))
    ext_var.set(item.get("extension", ""))

def add_or_update():
    config = load_config()
    key = name_var.get().strip()
    if not key:
        messagebox.showwarning("Warning", "Ransomware name cannot be empty.")
        return
    config[key] = {
        "description": desc_var.get(),
        "module": module_var.get(),
        "key_type": key_type_var.get(),
        "extension": ext_var.get()
    }
    save_config(config)
    refresh_list()
    messagebox.showinfo("Saved", f"Ransomware '{key}' saved successfully.")

def delete_selected():
    selection = listbox.curselection()
    if not selection:
        return
    key = listbox.get(selection[0])
    config = load_config()
    if key in config:
        del config[key]
        save_config(config)
        refresh_list()
        messagebox.showinfo("Deleted", f"'{key}' has been removed.")

# GUI setup
root = tk.Tk()
root.title("Ransomware Config Editor")
root.geometry("750x400")

listbox = tk.Listbox(root, width=25, height=20)
listbox.grid(row=0, column=0, rowspan=10, padx=10, pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

name_var = tk.StringVar()
desc_var = tk.StringVar()
module_var = tk.StringVar()
key_type_var = tk.StringVar()
ext_var = tk.StringVar()

labels = ["Name", "Description", "Module", "Key Type", "Extension"]
vars = [name_var, desc_var, module_var, key_type_var, ext_var]

for i, (label, var) in enumerate(zip(labels, vars)):
    tk.Label(root, text=label + ":").grid(row=i, column=1, sticky="w", padx=10)
    tk.Entry(root, textvariable=var, width=50).grid(row=i, column=2, padx=5, pady=3)

tk.Button(root, text="Save", bg="#4CAF50", fg="white", width=20, command=add_or_update).grid(row=6, column=2, pady=10)
tk.Button(root, text="Delete Selected", bg="#F44336", fg="white", width=20, command=delete_selected).grid(row=7, column=2)

refresh_list()
root.mainloop()
