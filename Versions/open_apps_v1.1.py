import subprocess
import time

# Function to open an application
def open_application(app_command):
    try:
        subprocess.Popen(app_command, shell=True)
        print(f"Opened {app_command}")
    except Exception as e:
        print(f"Failed to open {app_command}: {e}")

# Commands to open the applications
apps = [
    "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
    "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.exe",
    "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --restore-last-session",
    "\"C:\\Users\\Santosh Kumar Jha\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe\" --processstart 'Teams.exe' --newTeams",
    "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE\" \"D:\\OneDrive - Integer Telecom Services India Pvt. Ltd\\Integertel_Tracker.xlsx\"",
    "C:\Program Files\Amazon Web Services, Inc\Amazon WorkSpaces\\workspaces.exe"
]

# Open each application with a delay between them
for app in apps:
    open_application(app)
    time.sleep(2)  # Wait for 2 seconds before opening the next app
    