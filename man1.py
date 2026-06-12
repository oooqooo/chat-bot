# check for available models
import google.generativeai as genai

genai.configure(api_key="")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# ai access code 
import google.generativeai as genai

genai.configure(api_key="'")
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

print("AI Chatbot started. Type 'quit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit': break
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")

# read and respose on file content
import google.generativeai as genai
with open('nam`.txt') as f:  
     s = f.read()
genai.configure(api_key="")
model = genai.GenerativeModel('gemini-2.5-flash',system_instruction=f"You should respose using this {s}")
chat = model.start_chat(history=[])

print("AI Chatbot started. Type 'quit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit': break
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")

# own response code
knowledge = {}
with open("nam.txt", "r") as f:
    for line in f:
        if ":" in line:
            key, val = line.strip().split(":", 1)
            knowledge[key.lower()] = val


print("Simple Bot: I'm a non-AI bot. Type 'quit' to stop.")
while True:
    user_input = input("You: ").lower()
    if user_input == 'quit': break
    
    
    found = False
    for keyword in knowledge:
        if keyword == user_input:
            print(f"Bot: {knowledge[keyword]}")
            found = True           
            break
    if not found:
        print("Bot: I don't have that information in my file.")
