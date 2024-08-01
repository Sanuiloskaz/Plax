import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

scope = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing,playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri="https://callback.plax.app/",scope=scope))

current_volume = sp.current_playback()['device']['volume_percent']
last_volume = current_volume

def Function_Spotify_Pause():
    sp.pause_playback()

def Function_Spotify_Reproduce():
    sp.start_playback()

def Function_Spotify_Volume_Down():
    global current_volume
    if current_volume > 10:
        current_volume -= 10
    else:
        current_volume = 0
    sp.volume(current_volume)

def Function_Spotify_Volume_All():
    global current_volume
    current_volume = 100
    sp.volume(current_volume)

def Function_Spotify_Volume_Up():
    global current_volume
    if current_volume < 90:
        current_volume += 10
    else:
        current_volume = 100
    sp.volume(current_volume)

def Function_Spotify_Mute():
    global last_volume, current_volume
    last_volume = current_volume
    current_volume = 0
    sp.volume(current_volume)

def Function_Spotify_Unmute():
    global last_volume, current_volume
    current_volume = last_volume
    sp.volume(current_volume)

def Function_Spotify_Next_Song():
    sp.next_track()

def Function_Spotify_Last_Song():
    sp.previous_track()

def Function_Spotify_Reproduce_Song():
    pass

def Function_Spotify_Reproduce_Artist():
    pass

def Function_Spotify_Reproduce_Playlists():
    pass
