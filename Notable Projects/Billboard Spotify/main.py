import requests
import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
URL = "https://www.billboard.com/charts/hot-100/"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="2aad497880464194b72d931a643dc207",
        client_secret="a6a63ccee4604ca78a044fd30a14108b",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
date = input("Which Year do you want to travel to? Type the date in the format YYYY-MM-DD")
response = requests.get(url=f"{URL}{date}/")
soup = BeautifulSoup((response.text), "html.parser")

# songs = soup.find_all(name="h3", class_="c-title", id="title-of-a-story")
songs = soup.select(selector="li #title-of-a-story")
top_100 = [song.text.strip() for song in songs]
song_uri = []
for song in top_100:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)



# playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=True, collaborative=False,
#                                    description=f"Top 100 songs on the day {date}")
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
# # for uri in song_uri:
# #     sp.playlist_add_items(playlist_id=playlist["id"], items=uri)