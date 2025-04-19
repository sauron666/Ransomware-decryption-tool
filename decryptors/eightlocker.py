
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Known AES key and IV from 8locker samples
EIGHTLOCKER_KEY = b"8lockerEncryptKey"  # 16 bytes
EIGHTLOCKER_IV = b"8lockerEncryptIV!"  # 16 bytes

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        cipher = AES.new(EIGHTLOCKER_KEY, AES.MODE_CBC, EIGHTLOCKER_IV)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
