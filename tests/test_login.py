import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

from config import (
    BASE_URL,
    TEST_USER,
    TEST_PASS,
    BROWSER,
    HEADLESS
)


# 1. Menyiapkan browser sebelum pengujian
@pytest.fixture
def driver():

    if BROWSER == "edge":
        options = webdriver.EdgeOptions()

        if HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Edge(options=options)

    elif BROWSER == "chrome":
        options = webdriver.ChromeOptions()

        if HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(options=options)

    elif BROWSER == "firefox":
        options = webdriver.FirefoxOptions()

        if HEADLESS:
            options.add_argument("-headless")

        browser = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Browser tidak didukung: {BROWSER}")

    yield browser

    # Menutup browser setelah pengujian
    browser.quit()


# 2. Test case login valid
def test_login_valid(driver):

    # Membuka halaman login
    driver.get(f"{BASE_URL}/login")

    # Membuat objek LoginPage
    login_page = LoginPage(driver)

    # Melakukan login menggunakan konfigurasi environment
    login_page.login(TEST_USER, TEST_PASS)

    # Menunggu URL mengandung dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    # Memverifikasi keberhasilan login
    assert "/dashboard" in driver.current_url, (
        "Login gagal: URL tidak mengandung dashboard"
    )

    # Memverifikasi konten halaman Dashboard
    dashboard_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h1")
        )
    )

    assert dashboard_title.text == "Login Berhasil!", (
        "Dashboard gagal dimuat atau judul tidak sesuai"
    )

    # Membuat folder screenshots jika belum tersedia
    screenshot_dir = (
        Path(__file__).resolve().parents[1] / "screenshots"
    )

    screenshot_dir.mkdir(parents=True, exist_ok=True)

    # Menyimpan screenshot hasil pengujian
    screenshot_path = screenshot_dir / "hasil_login_pom.png"

    assert driver.save_screenshot(str(screenshot_path)), (
        "Screenshot gagal disimpan"
    )

    # Menampilkan informasi hasil pengujian
    print("\n====================================")
    print("HASIL PENGUJIAN AUTOMATION TESTING")
    print("====================================")
    print("Skenario :", "Login Valid")
    print("Username :", TEST_USER)
    print("URL      :", driver.current_url)
    print("Status   :", "PASS")
    print("Screenshot:", screenshot_path)
    print("====================================")