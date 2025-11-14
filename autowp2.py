import pyautogui
import pygetwindow as gw
import pyperclip
import time
import subprocess
import sys

contact_name = "Mummy"     # exact name as saved in WhatsApp contacts; leave empty to send to currently open chat
message = "Hello"
repeat_count = 20      # number of times to send the message

pyautogui.PAUSE = 0.12
pyautogui.FAILSAFE = True

def open_whatsapp_store():
    print("📱 Opening WhatsApp Desktop (Store app)...")
    subprocess.Popen(["explorer.exe", "shell:appsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])

def focus_whatsapp(timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        wins = gw.getWindowsWithTitle("WhatsApp")
        if wins:
            w = wins[0]
            try:
                w.activate()
            except Exception:
                try:
                    w.restore()
                    w.activate()
                except Exception:
                    pass
            time.sleep(0.6)
            return w
        time.sleep(0.4)
    return None

def open_chat_by_search(name):
    """Searches and opens a chat by contact name in WhatsApp Desktop (Store version)."""
    print(f"🔍 Searching for contact: {name}")
    pyautogui.hotkey("ctrl", "f")
    time.sleep(0.4)

    pyperclip.copy(name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.6)

    pyautogui.press("down")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(1.2)

    print(f"✅ Chat with '{name}' opened.")
    return True

def send_messages(msg, count):
    """Sends messages repeatedly to the open chat."""
    print(f"🚀 Sending '{msg}' {count} times...")
    for i in range(count):
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(0.15)
    print("All messages sent successfully.")

def main():
    open_whatsapp_store()
    w = focus_whatsapp(timeout=12)
    if not w:
        print("Could not find WhatsApp window. Please open WhatsApp manually and try again.")
        sys.exit(1)
    if contact_name.strip():
        open_chat_by_search(contact_name)
    else:
        print("💬 Sending to currently open chat...")
        
    time.sleep(1.5)
    send_messages(message, repeat_count)

if __name__ == "__main__":
    main()

