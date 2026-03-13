from database import load_users, save_users

username = input("Username: ")
password = input("Password: ")

users = load_users()

if username in users:
    print("User already exists.")
else:
    users[username] = password
    save_users(users)
    print("User registered successfully.")