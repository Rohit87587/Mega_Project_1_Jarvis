import pyautogui
import time
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os   

load_dotenv()

# ---------------------
# Gemini API Setup
# ---------------------
genai.configure(api_key=os.getenv("Gemini_api_key"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------
# Check last sender
# ---------------------
def is_last_message_from_sender(chat_log, sender_name="F Siddharth Vvp"):
    last_msg = chat_log.strip().split("/2025] ")[-1]
    return sender_name in last_msg


# ---------------------
# Main Loop
# ---------------------
time.sleep(1)

while True:
    time.sleep(8)

    # Select chat area
    pyautogui.moveTo(659, 189)
    pyautogui.dragTo(1901, 936, duration=2.0, button='left')

    # Copy selected text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)

    # Unselect area
    pyautogui.click(1876, 569)

    # Read chat
    chat_history = pyperclip.paste()
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    # Only reply if last message from target sender
    if is_last_message_from_sender(chat_history):

        prompt = f"""
You are a person named rohit.
Your style: funny roasting + Gujarati + English mix.
Analyze the chat history and reply with the next roast message.
Do NOT include timestamps like this: [10:28 am, 15/11/2025].
Chat History:
{chat_history}
"""

        # Generate reply using Gemini
        response = model.generate_content(prompt).text.strip()

        # Copy response to clipboard
        pyperclip.copy(response)

        # Click message box
        pyautogui.click(1005, 976)
        time.sleep(0.5)

        # Paste and send
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")
