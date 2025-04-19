
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Example leaked AES key and IV used by some Mamba variants
MAMBA_KEY = bytes.fromhex("00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF")
MAMBA_IV = bytes.fromhex("00000000000000000000000000000000")

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        cipher = AES.new(MAMBA_KEY, AES.MODE_CBC, MAMBA_IV)
        decrypted = cipher.decrypt(encrypted_data)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful (disk image): {output_path}")
    except Exception as e:
        print(f"Error: {e}")
