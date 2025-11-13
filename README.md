WhatsApp Auto Sender

A simple Python script that automatically sends messages through WhatsApp Desktop using PyAutoGUI and PyGetWindow.

📋 Features

Opens WhatsApp Desktop automatically

Focuses the app window

Sends your message multiple times

Works with any chat that’s already open

🧰 Requirements

Install these Python packages before running:

pip install pyautogui pygetwindow pyperclip

▶️ How to Use

Make sure WhatsApp Desktop is installed and logged in.

Open the chat where you want to send messages.

Run the script:

python autowp.py # to repeateadly send string in same Message
python autowp2.py # to send multiple messages


The script will send your message automatically.

⚙️ Configuration

You can edit these variables in the script:

message = "Hello!"      # Message to send
repeat_count = 10       # Number of times to send

⚠️ Note

This script only works with WhatsApp Desktop (from Microsoft Store), not WhatsApp Web.
