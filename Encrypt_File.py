from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet
import base64
import os


# Function to derive a key from a password
def derive_key(password: str):
    salt = os.urandom(16)
    # You can adjust the parameters for the KDF here
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt


# Function to encrypt the file
def encrypt_file(file_path: str, password: str):
    key, salt = derive_key(password)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(salt + encrypted)  # Prepend salt to encrypted data

    return encrypted_file_path


# Main function to handle encryption process
def main():
    file_path = input("Enter the path of the file to encrypt: ")
    password = input("Enter a password: ")
    encrypted_file_path = encrypt_file(file_path, password)
    print(f"File encrypted successfully and saved to {encrypted_file_path}")


if __name__ == "__main__":
    main()
