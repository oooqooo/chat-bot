import google.generativeai as genai
genai.configure(api_key="AIzaSyC0Jh4ROeqjKiAcC16mB6NZgEd2EsT-wAk")
v=genai.GenerativeModel('gemini-2.5-pro')
u=v.start_chat(history=[])

while True:
    a=input("you: ")
    if a.lower()=="quit":
        break
    b=u.send_message(a)
    print(f"gemin:{b.text}")