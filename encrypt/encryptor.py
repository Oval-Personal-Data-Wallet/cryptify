import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from sys import argv


def encode_file(file_path: str, pwd: str) -> str:

    if not pwd:

        pwd = Fernet.generate_key()

    with open(file_path, 'rb') as file:
        file_data = file.read()
        original_extension = os.path.splitext(file_path)[1].encode()

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(pwd))
    encrypted_key = base64.urlsafe_b64encode(key).decode()
    fernet = Fernet(key)
    encrypted_file_data = fernet.encrypt(file_data)

    encoded_file_data = encrypted_key.encode() + b":" + salt + b":" + \
        original_extension + b":" + encrypted_file_data

    encoded_file_path = os.path.splitext(file_path)[0] + ".ovl"
    with open(encoded_file_path, "wb") as encoded_file:
        encoded_file.write(encoded_file_data)

    return encoded_file_path


path = argv[1]
password = argv[2] if len(argv) > 2 else None


encode_file(path, password)
