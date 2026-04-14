# WhatsApp Auto Sender

## Overview

**WhatsApp Auto Sender** is a Python-based automation tool that sends messages through WhatsApp Desktop using GUI automation. It uses libraries like **PyAutoGUI**, **PyGetWindow**, and **Pyperclip** to control keyboard input and interact with the application window.

This tool allows users to send repeated messages or multiple custom messages automatically, reducing manual effort.

---

## Features

- **Automatically opens WhatsApp Desktop**
- **Detects and focuses the WhatsApp window**
- **Sends a single message multiple times**
- **Supports sending multiple custom messages**
- **Works with any chat that is already open**

---

## Tech Stack

- **Python**
- **PyAutoGUI**
- **PyGetWindow**
- **Pyperclip**

---

## Requirements

Install the required Python libraries:

```bash
pip install pyautogui pygetwindow pyperclip
````

---

## How to Use

1. Install **WhatsApp Desktop (Microsoft Store version)** and log in
2. Open the chat where you want to send messages
3. Run one of the scripts:

### Send Same Message Repeatedly

```bash
python autowp.py
```

### Send Multiple Messages

```bash
python autowp2.py
```

4. The script will automatically send messages to the selected chat

---

## Configuration

### For Repeated Message Script (`autowp.py`)

```python
message = "Hello!"        # Message to send
repeat_count = 10         # Number of times to send
```

### For Multiple Messages Script (`autowp2.py`)

```python
messages = ["Hi", "How are you?", "This is automated"]
```

---

## Limitations

* Works only with **WhatsApp Desktop (Microsoft Store version)**
* Requires the chat window to be open before running the script
* Performance may vary depending on system speed and screen resolution
* GUI automation may fail if the active window changes during execution

---

## Use Cases

* Sending repeated notifications
* Automating reminders
* Testing message automation workflows

