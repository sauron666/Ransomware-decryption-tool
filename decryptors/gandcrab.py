
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Example built-in GandCrab v5 private key (replace with actual one)
BUILTIN_KEYS = {
    "GANDCRAB_V5": """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCx8XClEzJZ5nR0EXAMPLEKEYw6cTFi9WIo0sHxl8yRkn0ryGp92
...
fR9jdVC39a8jSk+EwIDAQAB
-----END RSA PRIVATE KEY-----"""
}

def decrypt(file_path, key_name, output_path):
    try:
        if key_name not in BUILTIN_KEYS:
            print(f"Key '{key_name}' not found.")
            return
        rsa_key = RSA.import_key(BUILTIN_KEYS[key_name])
        rsa_cipher = PKCS1_OAEP.new(rsa_key)

        with open(file_path, "rb") as f:
            data = f.read()

        enc_session_key = data[:256]
        iv = data[256:272]
        encrypted_data = data[272:]

        session_key = rsa_cipher.decrypt(enc_session_key)
        aes_cipher = AES.new(session_key, AES.MODE_CBC, iv)
        decrypted = unpad(aes_cipher.decrypt(encrypted_data), AES.block_size)

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
