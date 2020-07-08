import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import pandas as pd

market = "US"
CLIENT_ID = "****************************"
CLIENT_SECRET = "*************************"
redirect_uri = 'http://localhost:8888/callback'
credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)
		
token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)
username = '*******'

excel_file = 'musiclib.xlsx'
music = pd.read_excel(excel_file)

for index, row in music.iterrows():
    track = row
    res = spotify.search(track, type="track", market=market, limit=1)
    s = str(res)
    tracker = s.find("spotify:track:")
    uri = s[tracker+14:tracker+36]
    print(uri)