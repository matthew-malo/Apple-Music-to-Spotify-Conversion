import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


market = "US"
CLIENT_ID = "********************"
CLIENT_SECRET = "********************"
username = '********************'
playlist_id = '********************'
scope = 'playlist-modify'
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri = "http://localhost:8888")

# Since the Spotipy API recommends only using Excel files with a maximum of 100 rows, I had to separate each batch of URIs
# into different spreadsheets, then load them in individually. I realize this process can be improved, and am attempting
# to optimize it. 
tracks = ["6C4LXC9UFH1IKiHYOp0BiJ",
"1VuBmEauSZywQVtqbxNqka",
"4uOKFydzAejjSFqYbv1XPt",
"0RFgvrhkf9FiDRLA0BhzpZ",
"1vfoYuejOS4RPcLbQdDKLH",
"2tAeN2TKlQLOoSPXtARzBV",
"3KhF2YiNpJvGpfiCW45R6D",
"1jFhnVoJkcB4lf9tT0rSZS",
"3yrSvpt2l1xhsV9Em88Pul",
"05RgAMGypEvqhNs5hPCbMS",
"6fybp4N6eW3bsFAvARxyVe",
"0TaT50ZZxT4ytZxuqkE3A9",
"48i055G1OT5KxGGftwFxWy",
"6QDbGdbJ57Mtkflsg42WV5",
"6OTPNDZ8FLCpe9Dyj66ajB",
"76ziL4M1nP9psv11be5812",
"18LhA0zBzAa2YnhcN3hWGa",
"4MM0jT9z9m7VFiusFrGJ8C",
"7bZQbORthYZpDnIddIDCcT",
"7kF1iPJTj3VFJX9XokQ80F",
"4cKGldbhGJniI8BrB3K6tb",
"2amzrvbxYiq8AxGntIiw5V",
"4sDKoZUpknYVeSJHdx8y1O",
"1bPeGzT9e95wpzs3ovNwFB",
"1ZuE6xOcK90eKdQ0EVC9gv",
"3XQY8kDjI8LARMIC9xkxQk",
"4w27lZ9zcceZp6rumzGCBx",
"3NYgTI7yMg9DBYUfCRuQP6",
"5tZmLjU4vhPlJb12IweZuB",
"0z1b34WikhOH9ZxU8QDWcv",
"5dWfl2PBpKHpBVdz95wxK1",
"0wVluBsVAVzBKrqspuCcwR",
"7fBv7CLKzipRk6EC6TWHOB",
"3mwvKOyMmG77zZRunnxp9E",
"2mPMFJvQ0v27gVqe5b6nDn",
"2MLHyLy5z5l5YRp7momlgw",
"6VoIBz0VhCyz7OdEoRYDiA",
"5WhtlIoxoZrMmuaWWEQhwV",
"3RiRFyvasDtAv8n0AQUKFG",
"6YK2tAEYnHgYkkC6TSziqM",
"2nlSeJ6CgvWeVOkrLmadf6",
"0weAUscowxeqDtpCgtbpgp",
"0odHj0qIf86vHBsXB30IkZ",
"3wGXyJGsCf1myH5MooQIqE",
"4tj8pey83vDcoXZYRSRBRc",
"7y5zXpTN4J7K0PngQYa655",
"2MU9jS03UMkLiHvxOYmKre",
"4m5zY9PRJvqPRDhDMJwSel",
"2wVaikw9WmhmIPyNt6BWa2",
"61mWefnWQOLf90gepjOCb3",
"3fQzTeYA61gdP4XN9vK7rb",
"4liGjmhCupa7RP9JaQELYx",
"3ee8Jmje8o58CHK66QrVC2",
"2w5IhsCbDMWzJw28qQuzm9",
"1OmKo4t4Bh95xQI6WGiUR3",
"2idmlkd8oUaQvYEtINpLBX",
"0B3FovCVaGKS5w1FTidEUP",
"2YEQNToSXA0iOxzpHPlkw9",
"6JzCO4ZzxAXhY86vTcqM1Q",
"23oxJmDc1V9uLUSmN2LIvx",
"7795WJLVKJoAyVoOtCWqXN",
"6Y9kdB2O0h9gq9y2vclsWT",
"3BPo7rn4wRUhysnUhccpqG",
"7qXTeIDkqZIexgdCXrxIrB",
"7qFxSPDUDMQNGBqTvK4aEj",
"57kdeoYzgGaKzRWj4XM1u8",
"3L0IKstjUgDFVQAbQIRZRv",
"0Ss50OU9tCozI7JIywkv14",
"2HJQcyUpmUuvzS5vBAICIc",
"5AJrhrwz4oSZX2PwwV4qrN",
"1UBQ5GK8JaQjm5VbkBZY66",
"4dK00wCxlqWEeN8BoM1BHT",
"0dbQ4h3cs8QE5fOPMYdDrX"]


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    for x in tracks:
        sp.user_playlist_add_tracks(username, playlist_id, x, position=None)

print("complete")
