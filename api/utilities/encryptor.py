import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

ACCEPTED_EXTENSIONS = ['txt', 'pdf', 'png',
                       'jpg', 'jpeg', 'docx', 'xlsx', 'md', 'py']


def encode_file(file_path):

    if not any(file_path.endswith(ext) for ext in ACCEPTED_EXTENSIONS):
        print(f"File extension not supported for file: {file_path}")
        return

    password = Fernet.generate_key()

    with open(file_path, 'rb') as file:
        file_data = file.read()
        original_extension = os.path.splitext(file_path)[1].encode()

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    encrypted_key = base64.urlsafe_b64encode(key).decode()
    fernet = Fernet(key)
    encrypted_file_data = fernet.encrypt(file_data)

    encoded_file_data = encrypted_key.encode() + b":" + salt + b":" + \
        original_extension + b":" + encrypted_file_data

    encoded_file_path = os.path.splitext(file_path)[0] + ".ovl"
    with open(encoded_file_path, "wb") as encoded_file:
        encoded_file.write(encoded_file_data)

    return encoded_file_path
