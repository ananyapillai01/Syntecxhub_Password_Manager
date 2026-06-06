Password Manager

A secure local password manager built using Python and cryptographic encryption techniques.

This project stores passwords in an encrypted JSON vault using AES-based encryption provided by Fernet. A master password is used to derive a secure encryption key with PBKDF2HMAC and SHA-256 hashing.

Features

* Master password authentication
* Secure password encryption
* Local encrypted storage
* Add password entries
* Retrieve stored passwords
* Delete password entries
* Search saved entries
* Command-line menu interface

Technologies Used

* Python
* JSON
* Cryptography Library
* PBKDF2HMAC
* Fernet Encryption (AES-based)

Security Concepts Used

PBKDF2 Key Derivation
The master password is converted into a strong cryptographic key using PBKDF2HMAC with 100000 iterations.

Salt Generation
A random salt is generated using `os.urandom()` to prevent identical password hashes.

Encryption
Passwords are encrypted using Fernet symmetric encryption before being stored locally.

Secure Password Input
`getpass()` is used to hide password input in the terminal.

Project Structure

password_manager/
-> main.py
-> vault.json
-> salt.key
-> .gitignore

How to Run

1. Clone the repository
git clone https://github.com/ananyapillai01/password-manager.git

2. Navigate into the project folder
cd password-manager

3. Install dependencies
pip install cryptography

4. Run the application
python main.py

Menu
PASSWORD MANAGER

1. Add Password
2. Retrieve Password
3. Delete Password
4. Search
5. Exit

Important Notes
* `vault.json` and `salt.key` are excluded from GitHub using `.gitignore`
* This project is intended for educational and internship purposes
* Passwords are stored locally on the user's machine

Future Improvements

* GUI version using Tkinter or PyQt
* Password strength checker
* Random password generator
* Auto-lock timeout
* Clipboard auto-clear
* Multi-user support
