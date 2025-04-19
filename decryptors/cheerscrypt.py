
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b'CHEERSCRYPTKEY00'
IV = b'CHEERSINITVECTOR'

def decrypt(file_path, key_name, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        decrypted = unpad(cipher.decrypt(data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
