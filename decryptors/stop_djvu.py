
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Offline master keys known to work for some STOP Djvu variants (hex encoded)
OFFLINE_KEYS = {
    "AES256_OFFLINE_KEY": bytes.fromhex("6A1D78E4B8D6D03C68340F4D7A822C81E20F6C3ED5D0C9F7C9D89E733F56D2C9")
}

def decrypt(file_path, key_name, output_path):
    try:
        if key_name not in OFFLINE_KEYS:
            print(f"Key '{key_name}' not found.")
            return
        key = OFFLINE_KEYS[key_name]
        with open(file_path, 'rb') as f:
            data = f.read()
        # Assuming STOP Djvu uses AES CBC with IV at start
        iv = data[:16]
        encrypted = data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
        with open(output_path, 'wb') as f:
            f.write(decrypted)
        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
