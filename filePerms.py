import os
import subprocess
import time
import threading
import csv

# Define the AD group name you want to check
ad_group_name = ""

# Define the root directory of your shared drive
shared_drive_root = r""

# Define the CSV filename to save the results
output_csv_filename = ad_group_name+"_output.csv"

# Flag to indicate when the search is finished
search_finished = False

def is_group_in_acl(path):
    try:
        # Use icacls command to check permissions
        result = subprocess.check_output(['icacls', path], universal_newlines=True)

        # Check if the AD group is listed in the ACL
        if ad_group_name in result:
            return True
    except subprocess.CalledProcessError:
        pass  # Ignore errors

    return False

def find_folders_for_ad_group(root):
    global search_finished
    with open(output_csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["AD Group", "Folder"])

        for dirpath, dirnames, filenames in os.walk(root):
            if is_group_in_acl(dirpath):
                csv_writer.writerow([ad_group_name, dirpath])
                #print(f"AD Group '{ad_group_name}' has access to folder: {dirpath}")

    # Set the search_finished flag to True when the search is completed
    search_finished = True

def loading_animation():
    animation = "|/-\\"
    i = 0
    while not search_finished:
        sys.stdout.write(f"\r{animation[i % len(animation)]} Searching...")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)

if __name__ == "__main__":
    # Start the loading animation in a separate thread
    import sys
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()

    # Start the search from the shared drive root
    find_folders_for_ad_group(shared_drive_root)

    # Wait for the search to finish and the animation thread to join
    animation_thread.join()

    # Clear the loading animation line
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()
