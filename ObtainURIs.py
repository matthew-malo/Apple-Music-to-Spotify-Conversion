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

# I ported my Apple Music library to an Excel sheet, as python works well with CSVs, and Apple Music does not offer many
# alternatives for accessing the data otherwise
excel_file = 'musiclib.xlsx'
music = pd.read_excel(excel_file)

# Spotify adds songs to playlists via the song's URI, a 22 character string that serves a song's unique identifier
# The search function returns a dictionary data object, consisting of only one key value pair: the key being a number,
# and the value pair being every single attribute for a song. In order to access the URI, I had to convert the result
# into a string, then grab the substring containing the URI via an offset. If the offset did not return the desired
# 22 character string, I knew the song did not exist on Spotify, and would not be able to add it to my library
# I decided therefore to print the results to the console, then copy/paste them to a new Excel file
for index, row in music.iterrows():
    track = row
    result = spotify.search(track, type="track", market=market, limit=1)
    s = str(result)
    tracker = s.find("spotify:track:")
    uri = s[tracker+14:tracker+36]
    print(uri)
