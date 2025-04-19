
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad

# Publicly leaked Avaddon private RSA key (shortened for example)
AVADDON_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDIfZRoUGv...
...your full leaked private key here...
-----END RSA PRIVATE KEY-----"""

def decrypt(file_path, key_name, output_path):
    try:
        rsa_key = RSA.import_key(AVADDON_PRIVATE_KEY)
        rsa_cipher = PKCS1_OAEP.new(rsa_key)

        with open(file_path, "rb") as f:
            data = f.read()

        enc_key_len = 256  # RSA-encrypted AES key
        iv_len = 16

        enc_session_key = data[:enc_key_len]
        iv = data[enc_key_len:enc_key_len + iv_len]
        encrypted_data = data[enc_key_len + iv_len:]

        session_key = rsa_cipher.decrypt(enc_session_key)
        cipher = AES.new(session_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
