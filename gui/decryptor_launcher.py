
import tkinter as tk
from tkinter import ttk
import os

# Create main app window
root = tk.Tk()
root.title("Universal Ransomware Decryptor - All Tools")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Frames for each tab
tabs = {
    "Single File Decrypt": ttk.Frame(notebook),
    "Mass Decryption": ttk.Frame(notebook),
    "Brute-force": ttk.Frame(notebook),
    "Auto-Detect": ttk.Frame(notebook),
    "Config Editor": ttk.Frame(notebook)
}

for name, frame in tabs.items():
    notebook.add(frame, text=name)

# Embedding external UIs as modules
def embed_gui(tab_frame, script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        code = compile(f.read(), script_path, 'exec')
        exec(code, {'__name__': '__main__', '__file__': script_path, '__tk_root__': tab_frame})

# Launch GUI modules in separate windows for now (until full embed)
tk.Label(tabs["Single File Decrypt"], text="Run: decryptor_gui.py").pack(pady=10)
tk.Label(tabs["Mass Decryption"], text="Run: decryptor_gui_mass.py").pack(pady=10)
tk.Label(tabs["Brute-force"], text="Run: decryptor_bruteforce.py").pack(pady=10)
tk.Label(tabs["Auto-Detect"], text="Run: decryptor_autodetect.py").pack(pady=10)
tk.Label(tabs["Config Editor"], text="Run: decryptor_config_editor.py").pack(pady=10)

# Optionally add buttons to launch them
def launch_script(path):
    os.system(f"python {path}")

tk.Button(tabs["Single File Decrypt"], text="Launch", command=lambda: launch_script("universal_decryptor/gui/decryptor_gui.py")).pack()
tk.Button(tabs["Mass Decryption"], text="Launch", command=lambda: launch_script("universal_decryptor/gui/decryptor_gui_mass.py")).pack()
tk.Button(tabs["Brute-force"], text="Launch", command=lambda: launch_script("universal_decryptor/gui/decryptor_bruteforce.py")).pack()
tk.Button(tabs["Auto-Detect"], text="Launch", command=lambda: launch_script("universal_decryptor/gui/decryptor_autodetect.py")).pack()
tk.Button(tabs["Config Editor"], text="Launch", command=lambda: launch_script("universal_decryptor/gui/decryptor_config_editor.py")).pack()

root.mainloop()
