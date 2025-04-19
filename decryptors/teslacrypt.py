
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# TeslaCrypt v3/v4 master AES key (publicly known)
TESLA_KEY = bytes.fromhex("56AAB9931A2213F3D207C6A9186FAC87E871C518A24A91C582FD38E8521C58E4")

def decrypt(file_path, key_name, output_path):
    try:
        key = TESLA_KEY
        with open(file_path, "rb") as f:
            data = f.read()

        # TeslaCrypt uses AES-256-CBC with IV prepended
        iv = data[:16]
        encrypted_data = data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
