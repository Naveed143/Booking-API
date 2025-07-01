from datetime import datetime
import pytz
import json
import os

classes = []
bookings = []

def load_classes_from_file():
    file_path = os.path.join(os.path.dirname(__file__), "seed_data.json")
    with open(file_path, "r") as f:
        raw_data = json.load(f)
        for item in raw_data:
            dt = datetime.fromisoformat(item["datetime"])
            if dt.tzinfo is None:
                dt = pytz.timezone("Asia/Kolkata").localize(dt)
            classes.append({
                "id": item["id"],
                "name": item["name"],
                "datetime": dt,
                "instructor": item["instructor"],
                "available_slots": item["available_slots"]
            })

load_classes_from_file()
