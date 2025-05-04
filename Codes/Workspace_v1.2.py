import subprocess
import time

def get_teams_version():
    """Retrieve the version number of Microsoft Teams using PowerShell."""
    try:
        output = subprocess.check_output(
            ['powershell', '-Command', 'Get-AppxPackage -Name MSTeams* | Select-Object -First 1 -ExpandProperty Version'],
            text=True,
            stderr=subprocess.STDOUT
        )
        version = output.strip()
        return version
    except subprocess.CalledProcessError as e:
        print(f"Error running PowerShell command: {e.output}")
        return None

def get_teams_path(version):
    """Construct the Teams executable path using the version number."""
    if version:
        # Construct package name assuming suffix '_x64__8wekyb3d8bbwe' is constant
        package_name = f"MSTeams_{version}_x64__8wekyb3d8bbwe"
        teams_path = f'"C:\\Program Files\\WindowsApps\\{package_name}\\ms-teams.exe"'
        return teams_path
    else:
        return None

def open_application(app_command):
    """Launch an application and handle potential errors."""
    try:
        subprocess.Popen(app_command, shell=True)
        print(f"Opened {app_command}")
    except Exception as e:
        print(f"Failed to open {app_command}: {e}")

# Get Teams version and construct path
version = get_teams_version()
teams_path = get_teams_path(version)

# List of applications to open
apps = [
    "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
    "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.exe",
    "\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --restore-last-session",
    "\"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE\" \"D:\\OneDrive - Integer Telecom Services India Pvt. Ltd\\Integertel_Tracker.xlsx\"",
    "C:\\Program Files\\Amazon Web Services, Inc\\Amazon WorkSpaces\\workspaces.exe"
]

# Insert Teams path if found
if teams_path:
    apps.insert(3, teams_path)
else:
    print("Microsoft Teams version not found. Skipping.")

# Launch all applications with a delay between each
for app in apps:
    open_application(app)
    time.sleep(2)

#pyinstaller --onefile --noconsole --icon=icon.ico open_apps.py
