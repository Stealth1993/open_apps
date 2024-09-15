Open Apps you regularly use on windows machine with a single click
This uses python's following modules:
-subprocess
-os
-pyinstaller (to create windows executable file)

Go to the yourfile.file directory, open command window or powershell and run this to create executable:
pyinstaller --onefile --noconsole open_apps.py
