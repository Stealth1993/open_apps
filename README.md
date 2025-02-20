# 🚀 **One-Click App Launcher for Windows**  

## **Launch Your Favorite Apps Instantly!** 🎯  
Tired of manually opening the same applications every day? This simple yet powerful Python script lets you launch all your frequently used Windows apps with just **one click**!  Create your workspace with ease.

---

## **🔧 How It Works**  
This script leverages Python’s built-in modules to automate app launching effortlessly:  
🔹 `subprocess` – Runs applications in the background  
🔹 `os` – Manages file paths and execution  
🔹 `time` – Adds delays for smooth sequential execution  

And for ultimate convenience, you can convert it into a **Windows executable** using **PyInstaller**.  

---

## **💻 Create an Executable (.exe)**  
Convert your Python script into a standalone `.exe` file by running:  
```bash  
pyinstaller --onefile --noconsole open_apps.py  
```  
Once compiled, just double-click the executable to launch your apps instantly!  

---

## **✨ What’s New in v2.0.1?**  
👉 **Auto-Check for Teams & Outlook Versions** – No more manual updates! The script detects installed versions and launches the correct one.  
👉 **Enhanced Customization** – Modify app paths easily to add more programs.  
👉 **Admin Privileges** – Runs with elevated permissions to ensure seamless execution.  

To generate an updated `.exe`, use:  
```bash  
pyinstaller --noconsole --onefile --uac-admin --icon=iran.ico open_apps_v2.py  
```  
This version intelligently detects **version changes** and adjusts accordingly!  

---

## **🎯 Customization & Setup**  
Want to add more apps? Simply update the script with their file paths, recompile, and you're all set!  

🔥 **Boost your productivity. Automate the boring stuff. Let technology work for you!** 🔥  

