import json
import os
from app.core.config import settings # <--- Import settings

def load_db():
    if not os.path.exists(settings.DB_FILE):
        return []
    with open(settings.DB_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_db(data):
    with open(settings.DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)