import google.generativeai as genai

API_KEY = 'AIzaSyDzIXdqe0nq-REU6Zcz8Ik52u7F3pFQd0o'

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

first_config = "Gemini, si te preguntan como te llamas por favor di Plax, y si te saludan con, por ejemplo, Hola plax, necesito que reconozcas ese nombre"

chat.send_message(first_config)

while(True):
    question = input("You: ")

    if(question.strip() == 'exit'):
        break

#    elif(question.strip())

    response = chat.send_message(question)
    print('\n')
    print(f'Bot: {response.text}')
    print('\n')