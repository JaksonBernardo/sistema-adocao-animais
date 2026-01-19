import os
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()

class Config:

    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "database")

BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_FILE = BASE_DIR / "settings.json"

with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
    SETTINGS_INFO = json.load(f)
