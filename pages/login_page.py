from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object Model for the login page."""
    def __init__(self, driver):
        self.driver = driver

    def load(self, login_URL):
        """Load the login page."""
        self.driver.get(login_URL)

    def login(self, email, password):
        """Perform login with email and password."""
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]'))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "email"))
        ).send_keys(email)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Continue']"))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]'))
        ).send_keys(password)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Sign in']"))
        ).click()

    def is_logged_in(self):
        """Verify if the user is logged in by checking the URL."""
        return WebDriverWait(self.driver, 30).until(
            EC.url_contains("/organizations")
        )
