import pytest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        browser = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Browser tidak didukung: {BROWSER}")

    yield browser

    browser.quit()


# 2. Test case login valid
def test_login_valid(driver):

    # Membuat folder screenshot
    screenshot_dir = (
        Path(__file__).resolve().parents[1] / "screenshots"
    )

    screenshot_dir.mkdir(parents=True, exist_ok=True)

    # Membuka halaman login
    driver.get(f"{BASE_URL}/login")

    # Membuat objek LoginPage
    login_page = LoginPage(driver)

    # Melakukan login
    login_page.login(TEST_USER, TEST_PASS)

    # Menunggu login berhasil atau gagal
    try:

        WebDriverWait(driver, 15).until(
            lambda d: (
                "/dashboard" in d.current_url
                or "Login Gagal!" in d.page_source
            )
        )

    except TimeoutException:

        # Screenshot jika proses login timeout
        driver.save_screenshot(
            str(screenshot_dir / "hasil_login_debug.png")
        )

        body_text = driver.find_element(
            By.TAG_NAME, "body"
        ).text

        pytest.fail(
            f"Login timeout!\n"
            f"URL: {driver.current_url}\n"
            f"Isi halaman: {body_text}"
        )

    # Memeriksa jika login ditolak
    if "Login Gagal!" in driver.page_source:

        driver.save_screenshot(
            str(screenshot_dir / "hasil_login_debug.png")
        )

        pytest.fail(
            "Login ditolak oleh aplikasi. "
            "Periksa kecocokan GitHub Secrets "
            "dengan kredensial aplikasi PythonAnywhere."
        )

    # Memverifikasi URL Dashboard
    assert "/dashboard" in driver.current_url, (
        "Login gagal: URL tidak mengandung dashboard"
    )

    # Memverifikasi judul Dashboard
    dashboard_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h1")
        )
    )

    assert dashboard_title.text == "Login Berhasil!", (
        "Dashboard gagal dimuat atau judul tidak sesuai"
    )

    # Menyimpan screenshot hasil pengujian
    screenshot_path = screenshot_dir / "hasil_login_pom.png"

    assert driver.save_screenshot(str(screenshot_path)), (
        "Screenshot gagal disimpan"
    )

    print("\n====================================")
    print("HASIL PENGUJIAN AUTOMATION TESTING")
    print("====================================")
    print("Skenario :", "Login Valid")
    print("Username :", TEST_USER)
    print("URL      :", driver.current_url)
    print("Status   :", "PASS")
    print("Screenshot:", screenshot_path)
    print("====================================")