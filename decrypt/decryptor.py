import base64

import cryptography.fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from sys import argv


def decode_file(encoded_file_path: str, pwd: bytes) -> str:

    # make sure file is an ovl file
    if not encoded_file_path.endswith(".ovl"):
        print("File is not an ovl file")

    with open(encoded_file_path, "rb") as encoded_file:
        encoded_file_data = encoded_file.read()

    salt, original_extension, encrypted_file_data = encoded_file_data.split(
        b":")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(pwd))

    fernet = Fernet(key)

    try:
        decrypted_file_data = fernet.decrypt(encrypted_file_data)

        decrypted_file_path = encoded_file_path[:-4] + original_extension.decode()

        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_file_data)
        return decrypted_file_path

    except cryptography.fernet.InvalidToken:
        print("Incorrect password")
        return ""


path = argv[1]
password = bytes(argv[2], 'utf-8') if len(argv) > 2 else None

print(decode_file(path, password))
