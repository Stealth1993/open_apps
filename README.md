Open Apps you regularly use on windows machine, with a single click.
This uses python's following modules:
-subprocess
-os
-time
#pyinstaller (to create windows executable file)

Go to the yourfile.file directory, open command window or powershell and run this to create executable:
pyinstaller --onefile --noconsole open_apps.py

v2.0.1
-Added auto chcek for Teams & Outlook versions.
-Need to run updated pyinstaller for the executable file.
#pyinstaller --noconsole --onefile --uac-admin --icon=iran.ico open_apps_v2.py