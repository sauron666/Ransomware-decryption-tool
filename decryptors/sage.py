
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad

# Public leaked private RSA key (shortened example)
SAGE_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC0QY...your full private key here...
-----END RSA PRIVATE KEY-----"""

def decrypt(file_path, key_name, output_path):
    try:
        rsa_key = RSA.import_key(SAGE_PRIVATE_KEY)
        rsa_cipher = PKCS1_OAEP.new(rsa_key)

        with open(file_path, "rb") as f:
            data = f.read()

        enc_key_len = 256
        iv_len = 16

        enc_session_key = data[:enc_key_len]
        iv = data[enc_key_len:enc_key_len + iv_len]
        encrypted_data = data[enc_key_len + iv_len:]

        session_key = rsa_cipher.decrypt(enc_session_key)
        aes_cipher = AES.new(session_key, AES.MODE_CBC, iv)
        decrypted = unpad(aes_cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
