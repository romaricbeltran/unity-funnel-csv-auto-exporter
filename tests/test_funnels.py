import pytest
import shutil
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.funnels_page import FunnelsPage

@pytest.mark.login
def test_login_success(driver):
    """Test successful login on Unity."""
    login_page = LoginPage(driver)
    login_URL = os.getenv("UNITY_LOGIN_URL")
    email = os.getenv("UNITY_EMAIL")
    password = os.getenv("UNITY_PASSWORD")
    
    login_page.load(login_URL)
    login_page.login(email, password)

    assert login_page.is_logged_in(), "Login failed."

@pytest.mark.export
def test_export_csv_with_date_in_filename(driver):
    """Test exporting CSV file with today date in filename."""
    funnels_page = FunnelsPage(driver)
    funnel_URL = os.getenv("UNITY_FUNNEL_URL")
    funnels_page.load(funnel_URL)

    download_path = os.path.join(os.path.abspath("."), "downloads")
    funnels_page.export_csv(download_path)
    
    files = os.listdir(download_path)
    funnel_file = next((f for f in files if f.endswith(".csv")), None)
    assert funnel_file is not None, "CSV file was not downloaded."

    today = datetime.now().strftime('%Y-%m-%d')
    assert today in funnel_file, f"The file name does not contain today's date: {funnel_file}"

@pytest.mark.parametrize("download_path", [
    pytest.param("./test_download1", id="path1"),
    pytest.param("./test_download2", id="path2")
])
@pytest.mark.export
def test_export_with_custom_path_and_date_in_filename(driver, download_path):
    """Test exporting CSV with custom download path and today date in filename."""
    driver.execute_cdp_cmd('Browser.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': download_path
    })

    # Create the temporary download directory manually.
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    driver.refresh()
    funnels_page = FunnelsPage(driver)
    funnels_page.export_csv(download_path)

    files = os.listdir(download_path)
    funnel_file = next((f for f in files if f.endswith(".csv")), None)
    assert funnel_file is not None, f"CSV file was not downloaded in {download_path}."

    today = datetime.now().strftime('%Y-%m-%d')
    assert today in funnel_file, f"File name does not contain today's date: {funnel_file}"
    
    # Delete the temporary download directory manually.
    if os.path.exists(download_path):
        shutil.rmtree(download_path)
