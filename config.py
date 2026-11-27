import os
from pathlib import Path
from dotenv import load_dotenv

# Menentukan lokasi folder proyek
BASE_DIR = Path(__file__).resolve().parent

# Membaca konfigurasi dari file .env
load_dotenv(BASE_DIR / ".env")

# Memeriksa variabel wajib
required_vars = [
    "BASE_URL",
    "TEST_USER",
    "TEST_PASS"
]

missing_vars = [
    var for var in required_vars
    if not os.getenv(var)
]

if missing_vars:
    raise ValueError(
        f"Variabel environment belum diisi: {missing_vars}"
    )

# Mengambil konfigurasi environment
BASE_URL = os.getenv("BASE_URL").rstrip("/")
TEST_USER = os.getenv("TEST_USER")
TEST_PASS = os.getenv("TEST_PASS")

# Mengatur browser
BROWSER = os.getenv("BROWSER", "chrome").lower()

if BROWSER not in ["chrome", "edge", "firefox"]:
    raise ValueError("Browser tidak didukung!")

# Mengatur mode headless
HEADLESS_VALUE = os.getenv("HEADLESS", "true").lower()

if HEADLESS_VALUE not in ["true", "false"]:
    raise ValueError("HEADLESS harus true atau false!")

HEADLESS = HEADLESS_VALUE == "true"