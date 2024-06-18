import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id="3984adba08b5423890c112d62689cad0", client_secret="51503a1dab224365949c617adae4ee38", redirect_uri="https://callback.plax.app/",scope=scope))


sp.pause_playback()
sp.volume(100)
sleep(2)
sp.volume(50)
sp.start_playback()
sleep(2)
sp.volume(100)