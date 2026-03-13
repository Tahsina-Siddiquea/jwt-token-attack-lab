import jwt
import argparse
from config_secure import SECRET_KEY, ALGORITHM
from logger import log_event

parser = argparse.ArgumentParser()
parser.add_argument("--token", required=True)
args = parser.parse_args()

try:
    decoded = jwt.decode(
        args.token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    print(f"Access granted. Welcome {decoded['user']}")

except Exception as e:
    log_event(f"Invalid token attempt: {args.token}")
    print("Access denied:", e)