# cryptify

A file encryption-decryption engine for secure file transmission over the custom .ovl file extension system.

## Description

Cryptify allows you to encrypt and decrypt files using a custom file extension system. The system is designed to be secure and easy to use. The system is designed to be used in a client-server model, where the client encrypts the file and sends it to the server, and the server decrypts the file to be used or stored.

Cryptify completely deconstructs a file into a complex `.ovl` file, which is then encrypted using a sophisticated encryption algorithm. The `.ovl` file disguises the contents and file type of the original file and the encryption algorithm makes it impossible to decrypt the file without the decryption engine. The `.ovl` file is then sent to the server, where it is decrypted and the original file is reconstructed.

Cryptify is designed to be used as a secure file transfer system, where the integrity of the file is maintained and the file is not tampered with. If the file is tampered with, the decryption will fail and the file will not be reconstructed. Also, if the `.ovl` file is intercepted during transmission, the file will be practically useless, as the `.ovl` file is encrypted and the contents are disguised and cannot be decrypted without the decryption engine.

All the files are encrypted using AES-256 encryption algorithm, which is a symmetric encryption algorithm. This means that the same key is used to encrypt and decrypt the file. The key is generated using the `os.urandom()` function, which generates a cryptographically secure random number. The key is then hashed using the SHA-256 hashing algorithm, which is a one-way hashing algorithm. This means that the key cannot be reversed to get the original key. The key is then encoded using the base64 encoding algorithm, which is a reversible encoding algorithm. This means that the key can be decoded to get the original key. The key is then stored in the `.ovl` file, which is then encrypted using the AES-256 encryption algorithm. The `.ovl` file is then sent to the server, where it is decrypted and the original file is reconstructed.

## Setup

- clone the repository

```bash
git clone https://github.com/buabaj/cryptify.git
```

- install the dependencies

```bash
pip install -r requirements.txt
```

- encrypt a file 

```bash
python3 encrypt/encryptor.py

```

- This will prompt you to enter the path to the file you want to encrypt. Enter the path and press enter.

- The file will be encrypted and a `.ovl` file will be created in the same directory as the original file.

- decrypt a file

```bash
python3 decrypt/decryptor.py
```

- This will prompt you to enter the path to the `.ovl` file you want to decrypt. Enter the path and press enter.

- The file will be decrypted and the original file will be reconstructed in the same directory as the `.ovl` file.

## Todo

[] Allow for users to encrypt and decrypt files using a password

[] create CLI tool

[] create API
