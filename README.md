🖥️ Python Desktop Automation Tool (Tkinter + PyAutoGUI)

A desktop automation tool built using Python, Tkinter, and PyAutoGUI.
This application automates repetitive tasks such as typing, messaging, Notepad workflows, WhatsApp automation, and retrieving screen information—making it useful for productivity, testing, and learning GUI automation.

📌 Features
✅ 1. Spam Message at Current Cursor

Automatically writes and sends a custom message multiple times where the cursor is focused.

✅ 2. Notepad Auto-Spam

Opens Notepad automatically

Types and spams a message

Sends repeated lines with delay and progress tracking

✅ 3. Check Screen Size

Shows your monitor's width and height using PyAutoGUI.

✅ 4. Notepad Cycle (Write → Delete → Close)

Performs a full workflow:

Opens Notepad

Types a message

Waits

Selects & deletes text

Closes Notepad without saving

✅ 5. WhatsApp Automation

Sends repeated messages to a selected contact on WhatsApp Desktop using automation (PyAutoGUI keyboard + mouse actions).

🔒 Safety Controls

This automation tool includes failsafe stops to prevent unwanted execution:

Move your mouse to the top-left corner → Automation stops

Press ESC (if the keyboard module is installed)

GUI shows status and stops when requested

🧰 Tech Stack
Component	Purpose
Python	Core language
Tkinter	GUI interface
PyAutoGUI	Mouse/keyboard automation
Keyboard (optional)	ESC key listener
subprocess	Opens Notepad
time	Delay management
📂 Project Structure
desktop-automation-tool/
│── automation_gui.py
│── README.md
│── requirements.txt


(Rename your main file to automation_gui.py for neatness—optional)

▶️ How to Run
1. Install dependencies
pip install pyautogui keyboard


If the keyboard module fails to install, the tool will still work—ESC stop is just disabled.

2. Run the tool
python automation_gui.py

📝 Usage Instructions
🔹 Run the script

A Tkinter control panel window opens.

🔹 Select any automation task:

Spam at cursor

Spam in Notepad

Get screen size

Notepad write→delete→close

WhatsApp message spam

Follow the on-screen prompts to enter:
✔ message
✔ contact name (for WhatsApp)
✔ spam count
✔ delay-based operations

🚀 Use Cases

Automating repeated typing tasks

WhatsApp Desktop testing

GUI automation demonstrations

Fast data entry

Python automation learning

Productivity workflows

⚠️ Disclaimer

This tool is for educational and productivity purposes only.
Avoid spamming or misuse that violates platform policies (WhatsApp, messaging apps, etc.).

📜 Author

Rekha Kaushik
Python Developer | Automation & AIML Enthusiast
