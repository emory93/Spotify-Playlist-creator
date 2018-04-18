import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
ID ="36c7a209b067434da55f981479211868"
secret = "32d9b60ce0c24a33bda5940e95c86c37"
username = "Mimicat"
client_credentials_manager = SpotifyClientCredentials(client_id=ID, client_secret=secret)
Spot = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)
if token:
    Spot = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
