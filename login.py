import jwt
import datetime
from database import load_users
from config_vulnerable import SECRET_KEY, ALGORITHM

username = input("Username: ")
password = input("Password: ")

users = load_users()

if username not in users or users[username] != password:
    print("Invalid credentials")
    exit()

payload = {
    "user": username,
    "role": "user",
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=5)
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

print("\nToken:")
print(token)