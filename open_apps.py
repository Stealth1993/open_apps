import subprocess
import time
import os

# Function to find application path
def find_application(executable_name, custom_path=None):
    if custom_path:
        # Check custom path first
        path = os.path.join(custom_path, executable_name)
        if os.path.isfile(path):
            return path

    # Check common paths
    common_paths = [
        os.path.join("C:\\Program Files", executable_name),
        os.path.join("C:\\Program Files (x86)", executable_name)
    ]
    
    # Check PATH environment variable
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)
    for dir in path_dirs:
        common_paths.append(os.path.join(dir, executable_name))
    
    for path in common_paths:
        if os.path.isfile(path):
            return path
    return None

# Function to open an application
def open_application(app_command, app_name):
    try:
        subprocess.Popen(app_command, shell=True)
        print(f"Opened {app_name}")
    except Exception as e:
        print(f"Failed to open {app_name}: {e}")

# Define paths directly
outlook_path = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.exe"
teams_path = r"C:\Users\YourUsername\AppData\Local\Microsoft\Teams\current\Teams.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Use Profile 2 for Chrome (update profile name if necessary)
if chrome_path:
    chrome_command = f"\"{chrome_path}\" --profile-directory=\"Santosh Jha\" --restore-last-session"
else:
    chrome_command = None

# List of applications to open
apps = [
    {"command": find_application("notepad++.exe", custom_path="C:\\Program Files\\Notepad++"), "name": "Notepad++"},
    {"command": outlook_path, "name": "Outlook"},
    {"command": chrome_command, "name": "Google Chrome"},
    {"command": teams_path, "name": "Teams"},
    {"command": "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE\" \"D:\\OneDrive - Integer Telecom Services India Pvt. Ltd\\Integertel_Tracker.xlsx\"", "name": "Excel"},
    {"command": find_application("workspaces.exe"), "name": "Amazon WorkSpaces"}
]

# Open each application with a delay between them
for app in apps:
    if app["command"]:
        print(f"Trying to open {app['name']} with command: {app['command']}")
        open_application(app["command"], app["name"])
    else:
        print(f"{app['name']} application not found")
    time.sleep(2)  # Wait for 2 seconds before opening the next app


#pyinstaller --onefile --noconsole open_apps.py