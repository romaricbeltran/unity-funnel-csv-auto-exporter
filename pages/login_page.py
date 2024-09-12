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
            EC.element_to_be_clickable((By.ID, ":r1:"))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "conversations_create_session_form_email"))
        ).send_keys(email)

        self.driver.find_element(By.ID, "conversations_create_session_form_password").send_keys(password)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Sign in']"))
        ).click()

    def is_logged_in(self):
        """Verify if the user is logged in by checking the URL."""
        return WebDriverWait(self.driver, 30).until(
            EC.url_contains("/organizations")
        )
