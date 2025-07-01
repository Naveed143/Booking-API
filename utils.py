import pytz
from datetime import datetime

def convert_to_timezone(dt: datetime, timezone_str: str) -> str:
    try:
        target_tz = pytz.timezone(timezone_str)
        return dt.astimezone(target_tz).strftime('%Y-%m-%d %H:%M %Z')
    except:
        return dt.strftime('%Y-%m-%d %H:%M %Z')
