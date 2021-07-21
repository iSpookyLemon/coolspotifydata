import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-read-private'

auth_manager = SpotifyOAuth("56e29977f200461aa722915d77084063", "1c22ce2ffd7f4e1fb6721d052973da9b", "http://example.com", scope=scope,)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print("%d %s" % (i, item['name']))