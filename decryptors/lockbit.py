
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad

def decrypt(file_path, key_name, output_path):
    try:
        with open(key_name, "rb") as kf:
            private_key = RSA.import_key(kf.read())
        rsa_cipher = PKCS1_OAEP.new(private_key)

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
