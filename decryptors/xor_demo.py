
def decrypt(file_path, key, output_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = bytes([b ^ key for b in data])
        with open(output_path, 'wb') as f:
            f.write(decrypted)
        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
