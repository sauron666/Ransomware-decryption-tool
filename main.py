import customtkinter as ctk
import os
from tkinter import filedialog, messagebox
import importlib
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DecryptorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Universal Ransomware Decryptor")
        self.geometry("1000x700")
        self.resizable(False, False)
        self.ransomware_list = self.load_config()
        self.splash = None
        self.show_splash()

    def show_splash(self):
        self.splash = ctk.CTkToplevel(self)
        self.splash.geometry("400x200")
        self.splash.title("Зареждане...")
        splash_label = ctk.CTkLabel(self.splash, text="Зареждане на декриптора...", font=("Arial", 18))
        splash_label.pack(expand=True)
        self.withdraw()
        self.after(1000, self.load_main_ui)

    def load_main_ui(self):
        if self.splash:
            self.splash.destroy()
        self.deiconify()
        self.build_ui()

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
            return list(config.keys())
        except:
            return []

    def build_ui(self):
        self.label_title = ctk.CTkLabel(self, text="Изберете вид ransomware:", font=("Arial", 18))
        self.label_title.pack(pady=10)

        self.ransomware_menu = ctk.CTkComboBox(self, values=self.ransomware_list)
        self.ransomware_menu.pack(pady=10)

        self.file_entry = ctk.CTkEntry(self, width=600, placeholder_text="Изберете криптиран файл")
        self.file_entry.pack(pady=5)
        self.browse_button = ctk.CTkButton(self, text="Преглед", command=self.select_file)
        self.browse_button.pack(pady=5)

        self.key_entry = ctk.CTkEntry(self, width=600, placeholder_text="Изберете ключов файл (.pem/.txt)")
        self.key_entry.pack(pady=5)
        self.key_button = ctk.CTkButton(self, text="Зареди ключ", command=self.select_key)
        self.key_button.pack(pady=5)

        self.decrypt_button = ctk.CTkButton(self, text="Декриптирай файл", command=self.run_decryptor)
        self.decrypt_button.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        self.log_box = ctk.CTkTextbox(self, height=200, width=900)
        self.log_box.pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_entry.delete(0, ctk.END)
            self.file_entry.insert(0, path)

    def select_key(self):
        path = filedialog.askopenfilename()
        if path:
            self.key_entry.delete(0, ctk.END)
            self.key_entry.insert(0, path)

    def run_decryptor(self):
        ransomware = self.ransomware_menu.get()
        file_path = self.file_entry.get()
        key_path = self.key_entry.get()
        output_path = filedialog.asksaveasfilename(defaultextension=".decrypted")

        if not ransomware or not file_path or not output_path:
            messagebox.showerror("Грешка", "Моля, попълнете всички полета.")
            return

        try:
            module = importlib.import_module(f"decryptors.{ransomware}")
            self.progress_bar.set(0.3)
            module.decrypt(file_path, key_path, output_path)
            self.progress_bar.set(1)
            self.log_box.insert(ctk.END, f"[+] Успешно декриптиране: {output_path}\n")
        except Exception as e:
            self.progress_bar.set(0)
            self.log_box.insert(ctk.END, f"[!] Грешка при декриптиране: {str(e)}\n")

if __name__ == "__main__":
    app = DecryptorApp()
    app.mainloop()