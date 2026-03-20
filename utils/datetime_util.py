from datetime import datetime

def current_time():
    return datetime.now().strftime("%d %b %Y %H:%M:%S")
