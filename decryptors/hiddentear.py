
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Default AES key and IV used by many HiddenTear variants
HIDDENTEAR_KEY = b"ThisIsA16ByteKey"
HIDDENTEAR_IV = b"ThisIsAnInitVect"

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        cipher = AES.new(HIDDENTEAR_KEY, AES.MODE_CBC, HIDDENTEAR_IV)
        decrypted = unpad(cipher.decrypt(data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
