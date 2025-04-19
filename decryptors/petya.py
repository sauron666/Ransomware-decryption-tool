
from Crypto.Cipher import Salsa20
import os

# Example known Salsa20 key and nonce (real Petya needs extracted values)
PETYA_KEY = b"0123456789ABCDEF0123"  # 20 bytes
PETYA_NONCE = b"12345678"  # 8 bytes

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        cipher = Salsa20.new(key=PETYA_KEY, nonce=PETYA_NONCE)
        decrypted = cipher.decrypt(encrypted_data)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful (boot/MFT): {output_path}")
    except Exception as e:
        print(f"Error: {e}")
