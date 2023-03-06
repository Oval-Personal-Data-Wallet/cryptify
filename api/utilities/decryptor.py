import os
import base64
from cryptography.fernet import Fernet


def decode_file(encoded_file_path):

    # make sure file is an ovl file
    if not encoded_file_path.endswith(".ovl"):
        print("File is not an ovl file")

    with open(encoded_file_path, "rb") as encoded_file:
        encoded_file_data = encoded_file.read()

    encrypted_key, salt, original_extension, encrypted_file_data = encoded_file_data.split(
        b":")
    encrypted_key = encrypted_key.decode()
    key = base64.urlsafe_b64decode(encrypted_key)
    fernet = Fernet(key)
    decrypted_file_data = fernet.decrypt(encrypted_file_data)

    decrypted_file_path = encoded_file_path[:-4] + original_extension.decode()
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_file_data)

    return decrypted_file_path
