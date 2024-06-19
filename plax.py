import google.generativeai as genai
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri="https://callback.plax.app/",scope=scope))

genai.configure(
    api_key = os.getenv("API_KEY")
)

start_volume = 100

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

first_config = "Gemini, si te preguntan como te llamas por favor di Plax, y si te saludan con, por ejemplo, Hola plax, necesito que reconozcas ese nombre."
sp.volume(start_volume)

chat.send_message(first_config)

def search():
    text = question.strip()
    word = "pon "
    position= text.find(word)
    query = text[position + len(word):]

    results = sp.search(q=query, type="track")
    song = results["tracks"]["items"][0]
    sp.start_playback(uris=[song["uri"]])

def chatbot():
    response = chat.send_message(question)
    print('\n')
    print(f'Bot: {response.text}')
    print('\n')

    

while True:
    question = input("You: ")

    if question.strip() == 'exit':
        break
    
    elif question.strip() == 'pausa':
        sp.pause_playback()

    elif question.strip() == 'reproduce':
        sp.start_playback()

    elif question.strip() == 'bajale':
        if start_volume <= 0:
            print("min vol")
        else:
            start_volume = start_volume-20
            sp.volume(start_volume)
    elif question.strip() == 'subele':
        if start_volume >= 100:
            print("max vol")
        else:
            start_volume = start_volume+20
            sp.volume(start_volume)
    elif question.strip() == 'silenciar':
        sp.volume(0)
    elif question.strip() == 'desmutea':
        sp.volume(start_volume)
    elif question.strip() == 'siguiente':
        sp.next_track()
    elif question.strip() == 'anterior':
        sp.previous_track()
    elif 'pon ' in question.strip():
        search()
    else:
        chatbot()