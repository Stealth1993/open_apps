import os
import subprocess
import time

# Function to open an application
def open_application(app_command):
    try:
        subprocess.Popen(app_command, shell=True)
        print(f"Opened: {app_command}")
    except Exception as e:
        print(f"Failed to open {app_command}: {e}")

# Function to find the latest version of a dynamically installed application
def find_latest_version(base_path, app_prefix, app_name):
    try:
        # Find folders starting with the app prefix
        app_folders = [folder for folder in os.listdir(base_path) if folder.startswith(app_prefix)]
        if app_folders:
            # Sort folders to get the latest version
            latest_folder = sorted(app_folders, reverse=True)[0]
            return os.path.join(base_path, latest_folder, f"{app_name}.exe")
    except PermissionError:
        print(f"Permission denied: {base_path}. Run as administrator to access this directory.")
    except FileNotFoundError:
        print(f"Directory not found: {base_path}")
    return None

# Paths to search
base_path = "C:\\Program Files\\WindowsApps"

# Find Microsoft Teams and Outlook dynamically
teams_path = find_latest_version(base_path, "MSTeams_", "ms-teams")
outlook_path = find_latest_version(base_path, "Microsoft.OutlookForWindows_", "olk")

# Static application paths
apps = [
    "C:\\Program Files\\Notepad++\\notepad++.exe",
    "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --restore-last-session",
    "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE\" \"D:\\OneDrive\\Tracker.xlsx\"",
    "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Amazon Web Services, Inc\\Amazon WorkSpaces\\workspaces.exe"
]

# Add Teams and Outlook to the list if found
if teams_path:
    apps.append(teams_path)
else:
    print("Microsoft Teams not found!")

if outlook_path:
    apps.append(outlook_path)
else:
    print("Outlook (new) not found!")

# Open each application with a delay between them
for app in apps:
    open_application(app)
    time.sleep(2)  # Wait for 2 seconds before opening the next app


#pyinstaller --onefile --noconsole --icon=iran.ico open_apps_v2.py
#pyinstaller --noconsole --onefile --uac-admin --icon=iran.ico open_apps_v2.py

