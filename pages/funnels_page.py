from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time
import os
import re

class FunnelsPage:
    """Page Object Model for the funnels page."""
    def __init__(self, driver):
        self.driver = driver

    def load(self, funnel_URL):
        """Load the funnel page."""
        self.driver.get(funnel_URL)

    def select_custom_date(self):
        """Select a custom date range."""
        date_range_button = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="date-range-filter"]'))
        ).find_element(By.CSS_SELECTOR, 'button[data-testid="main-button"]')
        
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(date_range_button)
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Custom']"))
        ).click()

        today = datetime.now().strftime('%b %d %Y')  # Format: Mar 01 2023

        end_date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='end-date']"))
        )
        
        end_date_input.click()
        end_date_input.send_keys("\uE003" * 15)  # Simulate 15 backspace to clear the field
        
        end_date_input.send_keys(today)
        self.driver.find_element(By.TAG_NAME, 'body').click()

        apply_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="applyFunnelButton"]'))
        )
        if not apply_button.is_enabled():
            raise Exception("Dates were not correctly validated.")

        apply_button.click()
        time.sleep(5)

    def glitch_display_export_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-root') and .//span[text()='Rename']]"))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='close']"))
        ).click()

        time.sleep(5)

    def wait_for_download_complete(self, download_dir, timeout=60):
        """Wait for the CSV file to be completely downloaded."""
        start_time = time.time()

        project_name = os.getenv("UNITY_PROJECT_NAME")
        sanitized_title = re.sub(r'\s+', '_', project_name.strip().lower())
        
        while True:
            files = os.listdir(download_dir)
            funnel_file_downloading = next(
                (
                    f for f in files
                    if re.search(rf"{re.escape(sanitized_title)}", f)
                    and (f.endswith('.crdownload') or f.endswith('.part'))
                ),
                None
            )

            if not funnel_file_downloading:
                break
            
            if time.time() - start_time > timeout:
                raise TimeoutError("Download Timeout.")

    def export_csv(self, download_dir):
        """Export the data to a CSV file and wait for it to complete downloading."""
        self.select_custom_date()
        #self.glitch_display_export_button()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="export-menu-button"]'))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-testid='export-to-csv']"))
        ).click()

        self.driver.find_element(By.TAG_NAME, 'body').click()

        self.wait_for_download_complete(download_dir)
        
        time.sleep(5)
