from config import (
    BASE_URL,
    TEST_USER,
    TEST_PASS,
    BROWSER,
    HEADLESS
)

print("=== HASIL PEMERIKSAAN ENVIRONMENT ===")

print("BASE_URL:", BASE_URL)
print("TEST_USER:", TEST_USER)
print("TEST_PASS:", "Terisi" if TEST_PASS else "Kosong")
print("BROWSER:", BROWSER)
print("HEADLESS:", HEADLESS)

print("\nKonfigurasi environment berhasil dibaca!")