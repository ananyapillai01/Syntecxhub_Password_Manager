import json
import os
import base64

from getpass import getpass

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

SALT_FILE = "salt.key"
VAULT_FILE = "vault.json"

def load_salt():

    if not os.path.exists(SALT_FILE):

        salt = os.urandom(16)

        with open(SALT_FILE, "wb") as f:
            f.write(salt)

    else:

        with open(SALT_FILE, "rb") as f:
            salt = f.read()

    return salt

def generate_key(master_password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )

    return key

def load_vault():
    
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "r") as f:

    try:
        return json.load(f)

    except json.JSONDecodeError:
        return {}

def save_vault(data):

    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=4)

salt = load_salt()

master_password = getpass("Enter master password: ")

key = generate_key(master_password, salt)

cipher = Fernet(key)

def encrypt_password(password):

    encrypted = cipher.encrypt(password.encode())

    return encrypted.decode()

def decrypt_password(encrypted_password):

    decrypted = cipher.decrypt(
        encrypted_password.encode()
    )

    return decrypted.decode()

def add_password():

    site = input("Enter site/app name: ")

    password = getpass("Enter password: ")

    encrypted = encrypt_password(password)

    vault = load_vault()

    vault[site] = encrypted

    save_vault(vault)

    print("Password saved successfully.")

def delete_password():

    site = input("Enter site/app name to delete: ")

    vault = load_vault()

    if site in vault:

        del vault[site]

        save_vault(vault)

        print("Password deleted successfully.")

    else:

        print("No entry found.")

def retrieve_password():

    site = input("Enter site/app name: ")

    vault = load_vault()

    if site in vault:

        decrypted = decrypt_password(vault[site])

        print("Password:", decrypted)

    else:

        print("No entry found.")

def search_entries():

    keyword = input("Search: ").lower()

    vault = load_vault()

    found = False

    for site in vault:

        if keyword in site.lower():

            print(site)

            found = True

    if not found:

        print("No matching entries.")

while True:

    print("\nPASSWORD MANAGER")

    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Search")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        add_password()

    elif choice == "2":

        retrieve_password()

    elif choice == "3":

        delete_password()

    elif choice == "4":

        search_entries()

    elif choice == "5":

        print("Exiting Password Manager.")

        break

    else:

        print("Invalid option.")
