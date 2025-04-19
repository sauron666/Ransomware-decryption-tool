
def decrypt(file_path, key_name, output_path):
    try:
        # Xorist XOR key can be passed as int or hex string
        key = int(key_name, 0)  # Accepts "0x..." or decimal

        with open(file_path, "rb") as f:
            data = f.read()

        decrypted = bytes([b ^ key for b in data])

        with open(output_path, "wb") as f:
            f.write(decrypted)

        print(f"Decryption successful: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
