import tkinter as tk
from tkinter import simpledialog, messagebox
import pyautogui
import time
import subprocess
# keyboard is optional
try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except Exception:
    KEYBOARD_AVAILABLE = False
# enable failsafe: move mouse to top-left corner to stop
pyautogui.FAILSAFE = True
# ---------- Helpers ----------
def ask_message_and_count(parent, msg_prompt="Enter the message:", count_prompt="How many times?"):
    msg = simpledialog.askstring("Input", msg_prompt, parent=parent)
    if not msg:
        return None, None
    count = simpledialog.askinteger("Input", count_prompt, parent=parent, minvalue=1)
    if not count:
        return None, None
    return msg.strip(), count
def check_stop():
    if KEYBOARD_AVAILABLE and keyboard.is_pressed("esc"):
        return True
    return False
def safe_sleep(seconds):
    end = time.time() + seconds
    while time.time() < end:
        if check_stop():
            return False
        time.sleep(0.1)
    return True
# ---------- Feature functions ----------
def spam_cursor():
    msg, count = ask_message_and_count(root, "Enter the message to spam:", "How many times to spam?")
    if not msg or not count:
        return
    for i in range(count):
        if check_stop():
            messagebox.showinfo("Stopped", "Automation stopped by user.")
            return
        pyautogui.write(msg, interval=0.05)
        pyautogui.press("enter")
        time.sleep(1)  # delay between messages
        # show progress on screen
        root.update()
        root.title(f"Spamming... {i+1}/{count}")
    messagebox.showinfo("Done", "Spamming complete!")
    root.title("Automation Control Panel - Safe")
def spam_notepad():
    msg, count = ask_message_and_count(root, "Enter the message to spam in Notepad:", "How many times to spam?")
    if not msg or not count:
        return
    subprocess.Popen("notepad.exe")
    time.sleep(2)
    pyautogui.click(x=400, y=400)  # adjust if needed
    for i in range(count):
        if check_stop():
            messagebox.showinfo("Stopped", "Automation stopped by user.")
            return
        pyautogui.write(msg, interval=0.05)
        pyautogui.press("enter")
        time.sleep(1)  # delay between messages
        root.update()
        root.title(f"Notepad Spamming... {i+1}/{count}")
    messagebox.showinfo("Done", "Spamming in Notepad complete!")
    root.title("Automation Control Panel - Safe")
def show_screen_size():
    w, h = pyautogui.size()
    messagebox.showinfo("Screen Size", f"Width: {w}, Height: {h}")
def notepad_cycle():
    msg = simpledialog.askstring("Input", "Enter the message to type in Notepad:", parent=root)
    if not msg:
        return
    subprocess.Popen("notepad.exe")
    time.sleep(2)
    pyautogui.click(x=400, y=400)
    pyautogui.write(msg, interval=0.1)
    if not safe_sleep(2):
        messagebox.showinfo("Stopped", "Automation stopped by user.")
        return
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    if not safe_sleep(1):
        messagebox.showinfo("Stopped", "Automation stopped by user.")
        return
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.3)
    pyautogui.press("n")  # don't save
    messagebox.showinfo("Done", "Message typed, deleted, and Notepad closed.")
def whatsapp_msg():
    contact = simpledialog.askstring("Input", "Enter contact name:", parent=root)
    if not contact:
        return
    msg, count = ask_message_and_count(root, "Enter the message to send:", "How many times to send?")
    if not msg or not count:
        return
    # open WhatsApp (taskbar shortcut index)
    pyautogui.hotkey("win", "9")
    time.sleep(5)
    pyautogui.write(contact, interval=0.08)
    time.sleep(2)
    # click contact at (314, 289)
    pyautogui.click(x=314, y=289)
    time.sleep(1)
    for i in range(count):
        if check_stop():
            messagebox.showinfo("Stopped", "Automation stopped by user.")
            return
        pyautogui.write(msg, interval=0.05)
        pyautogui.press("enter")
        time.sleep(1)  # delay between messages
        root.update()
        root.title(f"WhatsApp Spamming... {i+1}/{count}")
    messagebox.showinfo("Done", f"Message(s) sent to {contact}!")
    root.title("Automation Control Panel - Safe")
# ---------- GUI ----------
root = tk.Tk()
root.title("Automation Control Panel - Safe")
root.geometry("420x420")
tk.Label(root, text="Choose an Automation Task", font=("Arial", 14, "bold")).pack(pady=12)
tk.Button(root, text="Spam (Current Cursor)", width=34, command=spam_cursor).pack(pady=6)
tk.Button(root, text="Open Notepad & Spam", width=34, command=spam_notepad).pack(pady=6)
tk.Button(root, text="Get Screen Size", width=34, command=show_screen_size).pack(pady=6)
tk.Button(root, text="Notepad Cycle (Write-Delete-Close)", width=34, command=notepad_cycle).pack(pady=6)
tk.Button(root, text="Send WhatsApp Message", width=34, command=whatsapp_msg).pack(pady=6)
stop_text = "Stop options: Move mouse to top-left OR press ESC (if enabled)"
tk.Label(root, text=stop_text, font=("Arial", 9)).pack(pady=10)
root.mainloop()
