from groq import Groq

# Initialize client
client = Groq(api_key=" ")

# Example query
prompt = "Write a one-sentence bedtime story about a unicorn."

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # You can also use llama-3.1-8b-instant for faster speed
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
