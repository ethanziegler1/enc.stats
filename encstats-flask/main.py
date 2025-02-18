from flask import Flask, session, redirect, url_for, request, render_template
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(64)
if os.getenv("FLASK_ENV") == "production":
    redirect_uri = "https://encstats.vercel.app/callback"
else:
    redirect_uri = "http://127.0.0.1:5000/callback"
# 
client_id = "da6a918341704836931958964e9f8cf9"
client_secret = "f8e8786b555d446aa2cb28e3800234e3"
scope = "user-read-private user-read-email user-top-read user-read-recently-played user-library-read user-library-modify user-read-playback-state user-modify-playback-state"

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id,
    client_secret,
    redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True,
)
sp = Spotify(auth_manager=sp_oauth)


@app.route("/")
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for("get_data"))


@app.route("/get_data")
def get_data():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        return redirect(url_for("home"))
    user = sp.current_user()
    top_songs = sp.current_user_top_tracks(limit=10)["items"]
    top_albums = [
        album["album"] for album in sp.current_user_saved_albums(limit=10)["items"]
    ]
    top_artists = sp.current_user_top_artists(limit=10)["items"]
    return render_template(
        "data.html",
        user=user,
        top_songs=top_songs,
        top_albums=top_albums,
        top_artists=top_artists,
    )


@app.route("/callback")
def callback():
    sp_oauth.get_access_token(request.args["code"])
    return redirect(url_for("get_data"))


if __name__ == "__main__":
    app.run(debug=True)
