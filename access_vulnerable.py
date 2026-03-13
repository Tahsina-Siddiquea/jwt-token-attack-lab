import jwt
import argparse
from config_vulnerable import SECRET_KEY, VERIFY_SIGNATURE

parser = argparse.ArgumentParser()
parser.add_argument("--token", required=True)

args = parser.parse_args()

try:
    decoded = jwt.decode(
        args.token,
        SECRET_KEY,
        options={"verify_signature": VERIFY_SIGNATURE}
    )

    print(f"Access granted. Welcome {decoded['user']}")

except Exception as e:
    print("Access denied:", e)