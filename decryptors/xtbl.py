from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b"XTBLAESKEY00000".ljust(16, b"0")[:16]
IV = b"0000000000000000"

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()

        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error in xtbl: {e}")