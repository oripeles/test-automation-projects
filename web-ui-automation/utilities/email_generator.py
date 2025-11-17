import json
import random
import time
from pathlib import Path

DATA_FILE = Path("data/user_data.json")
def generate_unique_email():
    random_number = random.randint(1000, 9999)
    timestamp = int(time.time()) % 100000
    email = f"ori{random_number}{timestamp}.peles@gmail.com"

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["new_user"]["email"] = email

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return email

