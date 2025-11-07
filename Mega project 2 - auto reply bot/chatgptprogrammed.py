import pyautogui
import time
import pyperclip
from groq import Groq

# === SETTINGS ===
YOUR_NAME = "vasanth"   # Change if your name in chat is different
API_KEY = ""
CHECK_INTERVAL = 7      # Seconds between each check

# Chat window coordinates (adjust if needed)
SELECT_START = (1353, 1046)
SELECT_END = (1028, 977)
CHAT_BOX = (872, 976)
DESELECT_CLICK = (1241, 868)

client = Groq(api_key=API_KEY)

print("Vasanth's Auto Reply Bot Started!")
print("Press Ctrl + C to stop.\n")
time.sleep(2)

while True:
    try:
        # --- Focus chat safely (Alt + Tab to app) ---
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)

        # --- Select recent chat messages ---
        pyautogui.moveTo(*SELECT_START)
        pyautogui.dragTo(*SELECT_END, duration=0.8, button='left')
        time.sleep(0.3)

        # --- Copy selected text ---
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)
        copied_text = pyperclip.paste().strip()

        # --- Deselect (optional) ---
        pyautogui.click(*DESELECT_CLICK)
        time.sleep(0.3)

        if not copied_text:
            print("⚠️ No chat detected, retrying...")
            time.sleep(CHECK_INTERVAL)
            continue

        # --- Check last message ---
        lines = [l.strip() for l in copied_text.splitlines() if l.strip()]
        last_line = lines[-1] if lines else ""
        print(f"\n🕵️ Last message: {last_line}")

        # --- If last msg is from you, skip replying ---
        if YOUR_NAME.lower() in last_line.lower():
            print("🕒 Thunder sent last message — waiting for reply...")
            time.sleep(CHECK_INTERVAL)
            continue

        # --- Send the chat to AI for response ---
        print("💬 Generating reply...")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are Thunder’s auto-chat bot.
Reply naturally and casually, like Thunder would.
Keep responses short and human-like.
If message is funny, reply humorously.
If serious, reply respectfully.
Never mention AI or bots.
If confused, say something like 'wait fr?' or 'explain that again?'.
Use name 'Vasanth' only if needed."""
                },
                {"role": "user", "content": last_line},
            ],
        )

        reply_text = response.choices[0].message.content.strip()
        pyperclip.copy(reply_text)

        # --- Paste and send reply ---
        pyautogui.click(*CHAT_BOX)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.press('enter')

        print(f"✅ Replied: {reply_text}\n")
        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(5)
