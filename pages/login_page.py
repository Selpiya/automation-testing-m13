from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locator elemen halaman login
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, user, pwd):
        # Mengisi username
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        username_field.send_keys(user)

        # Mengisi password
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_field.send_keys(pwd)

        # Menekan tombol login
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()