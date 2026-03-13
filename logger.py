import datetime

LOG_FILE = "security_log.txt"

def log_event(event):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {event}\n")