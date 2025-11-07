import pyautogui
import time
import pyperclip
from groq import Groq

time.sleep(2)


pyautogui.click(1345, 1061)
time.sleep(1)


pyautogui.moveTo(712, 207)
pyautogui.dragTo(1546, 927, duration=1, button='left')
time.sleep(0.5)


pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

pyautogui.click(1241, 868)
time.sleep(0.3)


copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)

# Step 7: Send text to Groq AI for reply
client = Groq(api_key=" ")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": """Do not include time and name in chatchat in hinglish moer hindi but some english too say a deep quote sometimes and reply so much funny  You are now acting as my auto-reply bot. 
When someone sends a message, you will reply in a natural, friendly way as if you are me. 
Keep responses short, casual, and human-like — not robotic. 
If the message is funny, reply with humor; if it’s serious, reply respectfully. 
Don’t mention that you are an AI or bot. 
If someone asks for information or help, answer briefly and naturally. 
If you don’t understand something, just say something casual like “wait, what?” or “explain again?”. 
Use my name "thunder" if needed in context. 
Example tone: chill, confident, little bit playful but not cringe. i am 19"""
        },
        {"role": "user", "content": copied_text},
    ],
)


reply_text = response.choices[0].message.content
pyperclip.copy(reply_text)


pyautogui.click(872, 976)
time.sleep(0.5)


pyautogui.hotkey('ctrl', 'v')
time.sleep(0.2)
pyautogui.press('enter')

print("\nReply sent:")
print(reply_text)
