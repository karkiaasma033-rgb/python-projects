import hashlib
import json
import os
from getpass import getpass

FILENAME ="users.json"

def load_user():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(FILENAME, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(users):
    print("\n--- REGISTER ---")
    username = input("Choose username: ")
    if username in users:
        print("Username already exists!")
        return
    password = getpass("Choose password: ")
    confirm = getpass("Confirm password: ")
    if password != confirm:
        print("Passwords don't match!")
        return
    users[username] = hash_password(password)
    save_users(users)
    print(f"User {username} registered!")

def login(users):
    print("\n--- LOGIN ---")
    username = input("Username: ")
    if username not in users:
        print("User not found!")
        return
    password = getpass("Password: ")
    if users[username] == hash_password(password):
        print(f"Welcome back {username}!")
    else:
        print("Wrong password!")

users = load_user()

while True:
    print("\n1. Register 2. Login 3. Quit")
    choice = input("Choose: ")
    if choice == "1":
       register(users)
    elif choice == "2":
        login(users)
    elif choice == "3":
        break
 
