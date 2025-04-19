
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import glob
from tkinter.scrolledtext import ScrolledText
from helpers import validator

# Realistic brute-force logic using magic bytes
def brute_force_decrypt(file_path, keys_folder, ransomware_type, log_widget):
    if not os.path.exists(file_path) or not os.path.isdir(keys_folder):
        messagebox.showwarning("Warning", "Invalid file or key folder path.")
        return

    with open(file_path, "rb") as original:
        encrypted_data = original.read()

    key_files = glob.glob(os.path.join(keys_folder, "*"))
    log_widget.insert(tk.END, f"Found {len(key_files)} keys.\n")
    for key_file in key_files:
        try:
            with open(key_file, "rb") as kf:
                key_data = kf.read()

            # Simulated decrypt: XOR each byte with first byte of key for demo
            xor_key = key_data[0] if key_data else 0x00
            decrypted = bytes([b ^ xor_key for b in encrypted_data])

            if validator.is_probably_decrypted(decrypted):
                log_widget.insert(tk.END, f"Success with: {key_file}\n")
                with open(file_path + ".decrypted", "wb") as out:
                    out.write(decrypted)
                messagebox.showinfo("Key Found", f"Decryption key found: {key_file}")
                return
            else:
                log_widget.insert(tk.END, f"Key failed: {os.path.basename(key_file)}\n")
        except Exception as e:
            log_widget.insert(tk.END, f"Error with {key_file}: {str(e)}\n")

    log_widget.insert(tk.END, "No valid key found.\n")

# GUI Setup
root = tk.Tk()
root.title("Brute-force Ransomware Decryptor")
root.geometry("700x480")

tk.Label(root, text="Encrypted File:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
file_entry = tk.Entry(root, width=60)
file_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: file_entry.insert(0, filedialog.askopenfilename())).grid(row=0, column=2)

tk.Label(root, text="Folder with Keys:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
keys_entry = tk.Entry(root, width=60)
keys_entry.grid(row=1, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: keys_entry.insert(0, filedialog.askdirectory())).grid(row=1, column=2)

tk.Label(root, text="Ransomware Type:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
ransomware_combo = ttk.Combobox(root, values=["xor_demo", "stop_djvu", "gandcrab", "try_all"], state="readonly", width=57)
ransomware_combo.current(0)
ransomware_combo.grid(row=2, column=1, padx=5)

log_output = ScrolledText(root, height=15, width=85)
log_output.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Start Brute-force", bg="#FF5722", fg="white", height=2,
          command=lambda: brute_force_decrypt(file_entry.get(), keys_entry.get(), ransomware_combo.get(), log_output)
).grid(row=3, column=1, pady=10)

root.mainloop()
