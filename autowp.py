import pyautogui
import pygetwindow as gw
import pyperclip
import time
import subprocess

# Contact name (exactly as it appears in WhatsApp)
contact_name = "Mummy"   # change this

# Message to send
message = " Hiii " * 100

# --- Step 1: Open WhatsApp Desktop (Store version) ---
print(" Opening WhatsApp Desktop...")
subprocess.Popen(["explorer.exe", "shell:appsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])
time.sleep(8)  # wait for WhatsApp to open fully

# --- Step 2: Focus the WhatsApp window ---
windows = gw.getWindowsWithTitle("WhatsApp")
if windows:
    whatsapp_window = windows[0]
    whatsapp_window.activate()
    print(" WhatsApp window activated.")
else:
    print("WhatsApp window not found — make sure it’s open and you’re logged in.")
    exit()

# --- Step 3: Search for the contact ---
pyautogui.hotkey("ctrl", "f")
time.sleep(1)
pyautogui.press("enter")

# --- Step 4: Type and send message ---
time.sleep(1)
pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press("enter")

print(f"✅ Message sent successfully to {contact_name}!")

