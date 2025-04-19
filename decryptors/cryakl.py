
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Known AES key from leaked Cryakl/Fantom variants
CRYAKL_KEY = bytes.fromhex("ABCDEF9876543210ABCDEF9876543210ABCDEF9876543210ABCDEF9876543210")

def decrypt(file_path, key_name, output_path):
    try:
        key = CRYAKL_KEY
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
