import google.generativeai as genai
from time import sleep
from dotenv import load_dotenv
import os
import spotify_controls as sc
import re

functions_dictionary = {
    'Spotify_Pause': sc.Function_Spotify_Pause,
    'Spotify_Reproduce': sc.Function_Spotify_Reproduce,
    'Spotify_Volume_Down': sc.Function_Spotify_Volume_Down,
    'Spotify_Volume_Up': sc.Function_Spotify_Volume_Up,
    'Spotify_Volume_All': sc.Function_Spotify_Volume_All,
    'Spotify_Mute': sc.Function_Spotify_Mute,
    'Spotify_Unmute': sc.Function_Spotify_Unmute,
    'Spotify_Next_Song': sc.Function_Spotify_Next_Song,
    'Spotify_Last_Song': sc.Function_Spotify_Last_Song,
    'Spotify_Reproduce_Song': sc.Function_Spotify_Reproduce_Song,
    'Spotify_Reproduce_Artist': sc.Function_Spotify_Reproduce_Artist,
    'Spotify_Reproduce_Playlists': sc.Function_Spotify_Reproduce_Playlists
}







load_dotenv()

configuration_path = "configuration.txt"

if os.path.exists(configuration_path):

    with open(configuration_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

else:
    print("Error to find configuration file")

first_config = file_content

genai.configure(
    api_key = os.getenv("API_KEY")
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

chat.send_message(first_config)

#def artist_or_song():
    #entry = question.strip()
#    aos = f"{entry} es canción o artista"
 #   query = chat.send_message(aos)
  #  if query.text == "Artista":
    #    search_artist()
   # elif query.text == "Canción":
     #   search_song()
    #else:
      #  print("didn't found")

#def search_artist():
 #   text = question.strip()
  #  word = "pon "
   # position= text.find(word)
   # query = text[position + len(word):]

    #artist_id = sp.search(q=query, type="artist")["artists"]["items"][0]["id"]
    #sp.start_playback(context_uri=f"spotify:artist:{artist_id}")

#def search_song():
#    text = question.strip()
 #   word = "pon "
  #  position= text.find(word)
   # query = text[position + len(word):]

    #results = sp.search(q=query, type="track")
  #  song = results["tracks"]["items"][0]
   # sp.start_playback(uris=[song["uri"]])

#def search_playlist():
 #   text = question.strip()
  #  query = text.replace("playlist ", "")
   # results = sp.search(q=query, type="playlist")
#    playlist = results["playlists"]["items"][0]["uri"]
 #   sp.start_playback(context_uri=playlist)

def functions():
    intro = response.text.replace("¤", "").split('\n')
    run_function = functions_dictionary.get(intro[0])
    if run_function:
        run_function()
    else:
        print("error con eso pe")

def numbers(itsafunction):
    look = re.compile(r'\d')
    return bool(look.search(itsafunction))

def chatbot():  
    global response
    global itsafunction
    global the_function
    response = chat.send_message(question)
    print('\n')
    print(f'bot: {response.text}')

    if "¤" in response.text:
        itsafunction = response.text
        if numbers(itsafunction):
            op = response.text.split('\n')
            second_op = op[0].split('x')
            the_function = second_op[0]
            second_op_fixed = second_op[1].replace('x', '')
            int_number = int(second_op_fixed)
            n = 0
            while n <= int_number:
                functions()
                n += 1
        else:
            functions()
            op = response.text.split('\n')
            print(op[1])
            print('\n')

    else:
        print(f'Bot: {response.text}')
        print('\n')

def startup():
    chat.send_message(f'¤Data:volumen={sc.current_volume}%')

startup()

while True:
    question = input("You: ")
    
    chatbot()
