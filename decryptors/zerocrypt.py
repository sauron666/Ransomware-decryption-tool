
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Example static AES key and IV used in early ZeroCrypt variants
ZEROCRYPT_KEY = b"ZerocryptAES256!!ZerocryptAES256!!"[:32]  # 32 bytes
ZEROCRYPT_IV = b"InitVectorZC2020"  # 16 bytes

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        cipher = AES.new(ZEROCRYPT_KEY, AES.MODE_CBC, ZEROCRYPT_IV)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
