
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Example AES key used in known Nemucod samples
NEMUCOD_KEY = b"0123456789abcdef"  # 16-byte key

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        cipher = AES.new(NEMUCOD_KEY, AES.MODE_ECB)
        decrypted = unpad(cipher.decrypt(data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
