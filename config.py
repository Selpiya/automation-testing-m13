import os
from pathlib import Path
from dotenv import load_dotenv

# Menentukan lokasi folder proyek
BASE_DIR = Path(__file__).resolve().parent

# Membaca file .env
load_dotenv(BASE_DIR / ".env")

# Memeriksa variabel yang wajib tersedia
required_vars = [
    "BASE_URL",
    "TEST_USER",
    "TEST_PASS",
    "BROWSER",
    "HEADLESS"
]

missing_vars = [
    var for var in required_vars
    if not os.getenv(var)
]

if missing_vars:
    raise ValueError(
        f"Variabel environment belum diisi: {missing_vars}"
    )

# Mengambil nilai konfigurasi
BASE_URL = os.getenv("BASE_URL")
TEST_USER = os.getenv("TEST_USER")
TEST_PASS = os.getenv("TEST_PASS")
BROWSER = os.getenv("BROWSER").lower()

# Mengubah string menjadi Boolean
HEADLESS = os.getenv("HEADLESS").lower() in (
    "true", "1", "yes", "on"
)