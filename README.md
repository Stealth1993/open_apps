---

One-Click App Launcher for Windows 🚀

Simplify Your Workflow

Tired of opening multiple apps manually every day? This Python script lets you launch your most-used applications with just a single click!


---

How It Works

This script automates the process using Python’s built-in modules:
✅ subprocess – To run applications seamlessly
✅ os – To manage file paths
✅ time – To introduce necessary delays for a smooth launch

To make it even more convenient, you can package it into a Windows executable using PyInstaller.


---

Creating an Executable (.exe)

Convert the script into a standalone application with the following command:

pyinstaller --onefile --noconsole open_apps.py

Once generated, simply double-click the .exe file to launch your selected apps instantly!


---

What's New in v2.0.1? 🎉

🚀 Smart App Detection – Automatically checks for the latest versions of Microsoft Teams & Outlook before launching.
🔧 Enhanced Customization – Easily update app paths for other applications.
⚡ Admin Mode Execution – Ensures smooth operation by running with the necessary permissions.

To generate the updated executable, use:

pyinstaller --noconsole --onefile --uac-admin --icon=iran.ico open_apps_v2.py

This version dynamically detects changes in app versions and adjusts accordingly.


---

Setup & Customization

Want to add more applications? Just update the script with their file paths, recompile the .exe, and enjoy hassle-free launching!

🚀 Boost productivity. Save time. Let automation do the work! 🚀


---

This version makes your README more engaging, structured, and clear while keeping it professional and informative. Let me know if you'd like any further refinements!

