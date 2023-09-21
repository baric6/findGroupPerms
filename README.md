# Active Directory Group Folder Access Checker

This Python script allows you to search for folders within a shared drive and determine whether a specified Active Directory (AD) group has access to each folder. It then saves the search results to a CSV file.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Appropriate permissions to execute the `icacls` command on the shared drive.

## Configuration

1. Open the script file (`ad_group_folder_checker.py`) in a text editor.
2. Modify the following configuration variables at the beginning of the script:

   - `ad_group_name`: Replace with the name of the AD group you want to check.
   - `shared_drive_root`: Replace with the root directory of your shared drive.
   - `output_csv_filename`: Replace with the desired name of the CSV file where the results will be saved.

## How to Use

1. Save the modified script file.
2. Open a command prompt or terminal window.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python ad_group_folder_checker.py

    The script will start searching for folders accessible by the specified AD group.
    A loading animation will be displayed in the console to indicate the progress of the search.
    Once the search is complete, the results will be saved in the specified CSV file.
    You can access the results in the CSV file for further analysis.

Example Results

The CSV file will contain two columns:

    "AD Group": The name of the specified AD group.
    "Folder": The path to the folder that the AD group has access to.

Notes

    This script uses the icacls command to check folder permissions. Ensure that the icacls command is available and executable on your system.
    The script runs in a separate thread to display the loading animation while the search is in progress.
    Make sure to replace the configuration variables with appropriate values before running the script.
