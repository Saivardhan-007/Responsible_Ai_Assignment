"""
Task 1 - Version B (Revised, secure version)
Stores user data (name, email, hashed password) in a file.
Password is never stored or compared in plain text.
"""

import hashlib
import os
import binascii


def hash_password(password: str) -> str:
    """Hash a password with a random salt using PBKDF2-HMAC-SHA256."""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    # store salt + hash together, separated by ':'
    return binascii.hexlify(salt).decode() + ":" + binascii.hexlify(key).decode()


def verify_password(stored_hash: str, password_attempt: str) -> bool:
    """Check a login attempt against the stored salted hash."""
    salt_hex, key_hex = stored_hash.split(":")
    salt = binascii.unhexlify(salt_hex)
    expected_key = binascii.unhexlify(key_hex)
    attempt_key = hashlib.pbkdf2_hmac("sha256", password_attempt.encode(), salt, 100_000)
    return attempt_key == expected_key


def save_user(name, email, password):
    hashed = hash_password(password)
    with open("users_secure.txt", "a") as f:
        f.write(f"{name},{email},{hashed}\n")


def load_users():
    users = []
    with open("users_secure.txt", "r") as f:
        for line in f:
            name, email, hashed = line.strip().split(",")
            users.append({"name": name, "email": email, "password_hash": hashed})
    return users


if __name__ == "__main__":
    save_user("Saivardhan", "sai@example.com", "mypassword123")
    users = load_users()
    print(users)

    # Example login check
    attempt = "mypassword123"
    print("Login success:", verify_password(users[0]["password_hash"], attempt))
