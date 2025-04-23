import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

#code for encrypting the file
def encrypt_file(filename: str, password: str):
    with open(filename, 'rb') as f:
        data = f.read()

    salt = os.urandom(16)
    iv = os.urandom(16)
    key = derive_key(password, salt)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_blob = salt + iv + encrypted_data
    with open(filename + '.enc', 'wb') as f:
        f.write(encrypted_blob)
    print(f"File encrypted successfully as {filename}.enc")

#code for decrypting the file
def decrypt_file(filename: str, password: str):
    with open(filename, 'rb') as f:
        encrypted_blob = f.read()

#initating the salt value
    salt = encrypted_blob[:16]
    iv = encrypted_blob[16:32]
    encrypted_data = encrypted_blob[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    output_filename = filename.replace('.enc', '') + '.dec'
    with open(output_filename, 'wb') as f:
        f.write(data)
    print(f"File decrypted successfully as {output_filename}")


# Example Usage:
# encrypt_file('example.txt', 'my_secure_password')
# decrypt_file('example.txt.enc', 'my_secure_password')
#codebyvasan