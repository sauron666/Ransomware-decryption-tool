
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Example offline key used by some older Dharma variants (replace with real if needed)
DHARMA_KEY = bytes.fromhex("00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF")

def decrypt(file_path, key_name, output_path):
    try:
        key = DHARMA_KEY
        with open(file_path, "rb") as f:
            data = f.read()

        iv = data[:16]
        encrypted_data = data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
