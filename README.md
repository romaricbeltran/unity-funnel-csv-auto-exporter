# Unity Funnel CSV Auto Exporter

This project automates the process of logging into Unity, selecting a custom date range on the analytics funnels page, and exporting the data as a CSV file. It uses Selenium for browser automation and supports scheduling CSV downloads at regular intervals.

## Features

- Automates Unity login using Selenium WebDriver
- Selects a custom date range on the funnels page
- Exports analytics data as a CSV file
- Supports custom download paths
- Uses environment variables for configuration
- Includes scheduling capabilities (e.g., periodic CSV downloads)

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (Make sure the version matches your Chrome version)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/romaricbeltran/unity-funnel-csv-auto-exporter.git
    cd unity-funnel-csv-auto-exporter
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file based on the example provided:

    ```bash
    cp .env.example .env
    ```

5. Update the `.env` file with your Unity login credentials and the appropriate URLs.

    ```bash
    UNITY_LOGIN_URL="https://cloud.unity.com/home/login"
    UNITY_FUNNEL_URL="YOUR_FUNNEL_PAGE_URL"
    UNITY_PROJECT_NAME="YOUR_PROJECT_NAME"
    UNITY_EMAIL="your_email@domain.com"
    UNITY_PASSWORD="your_password"
    ```

## Environment Variables

The project uses environment variables to securely store sensitive information like Unity credentials and URLs. Here are the environment variables you need to set in the `.env` file:

- **UNITY_LOGIN_URL**: The URL of the Unity login page.
- **UNITY_FUNNEL_URL**: The URL of the Unity funnels page where data will be exported.
- **UNITY_PROJECT_NAME**: The project name where the Unity funnel is located.
- **UNITY_EMAIL**: Your Unity account email.
- **UNITY_PASSWORD**: Your Unity account password.

You can create the `.env` file based on the `.env.example` provided in the repository.

## Usage

### Run a CSV Export Once

To run the script and download the CSV once, you can use the following command:

```bash
python download_csv.py <destination_path>
```

Example:

```bash
python download_csv.py ./downloads
```

This will download the CSV file to the `./downloads` folder.

### Scheduling the CSV Export

The project supports scheduled CSV exports at regular intervals. By default, the script is configured to download a new CSV everyday at 6 AM. To enable this, just keep the script running:

```bash
python download_csv.py <destination_path>
```

You can modify the scheduling logic in the `download_csv.py` file by changing this part of the code:

```bash
schedule.every().day.at("06:00").do(download_and_update_csv, destination_path=destination)
```

For more information on scheduling tasks with schedule, check the schedule documentation.

## Project Structure

- `pages/`: Contains the Page Object Model (POM) classes for the login and funnels pages.
    - `funnels_page.py`: Handles the funnel page interactions, including the export of CSV files.
    - `login_page.py`: Automates the login process.
- `tests/`: Unit and integration tests.
    - `conftest.py`: Configures fixtures and browser setup for tests.
    - `test_funnels.py`: Tests related to the login and CSV export functionalities.
- `utils/`: Helper functions for browser setup and file management.
    - `browser_setup.py`: Configures the Selenium WebDriver with Chrome.
    - `file_management.py`: Handles file searching and renaming after export.
- `.env.example`: Template file for environment variables. Rename to `.env` and update with your own credentials.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `download_csv.py`: Main script to automate CSV export and scheduling.
- `pytest.ini`: Configuration file for pytest with custom markers.
- `requirements.txt`: Lists the Python packages required for the project.


## Running Tests
You can run tests using pytest. Ensure the appropriate test files and configurations are set up before running the command.

```bash
pytest
```

## Logging
The script uses Python's built-in logging module to log important events such as login success/failure, CSV export status, and file download paths. Log messages will be displayed in the terminal.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

