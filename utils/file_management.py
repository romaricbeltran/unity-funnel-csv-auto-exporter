import os
import re

def find_and_rename_file(download_dir, file_name=None):
    """Find and rename the downloaded CSV file."""
    funnel_title = os.getenv("UNITY_PROJECT_NAME")

    files = os.listdir(download_dir)
    funnel_file = next((f for f in files if re.search(rf"{re.escape(funnel_title)}.*\.csv$", f)), None)

    if not funnel_file:
        raise FileNotFoundError("Funnel CSV file not found.")

    final_file_name = file_name if file_name else funnel_file
    source_file = os.path.join(download_dir, funnel_file)
    destination_file = os.path.join(download_dir, final_file_name)
    os.rename(source_file, destination_file)
    return destination_file
