import google.generativeai as genai

API_KEY = 'AIzaSyDzIXdqe0nq-REU6Zcz8Ik52u7F3pFQd0o'

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

first_config = "Gemini, te llamare plax, y si por ejemplo te pregunto como te llamas me dices plax"

chat.send_message(first_config)

while(True):
    question = input("You: ")

    if(question.strip() == 'exit'):
        break

    response = chat.send_message(question)
    print('\n')
    print(f'Bot: {response.text}')
    print('\n')