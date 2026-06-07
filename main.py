import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Paste your credentials here
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8888/callback"

# Scope needed to control playback state natively
SCOPE = "user-modify-playback-state user-read-playback-state"

def play_spotify_music(search_query):
    # Clean the query
    query = search_query.replace('play', '').strip()
    if not query:
        return

    # Authenticate via Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

    print(f"Searching Spotify for: '{query}'...")
    
    # 1. Search for the track
    results = sp.search(q=query, limit=1, type='track')
    tracks = results['tracks']['items']
    
    if not tracks:
        print("No tracks found.")
        return
        
    track_uri = tracks[0]['uri']
    track_name = tracks[0]['name']
    artist_name = tracks[0]['artists'][0]['name']
    
    print(f"Found: {track_name} by {artist_name}")

    try:
        # 2. Tell Spotify's backend to immediately play this track on your active device
        sp.start_playback(uris=[track_uri])
        print(" Playing now...")
    except Exception as e:
        print("\nError: No active Spotify device detected.")
        print("Make sure you have a Spotify endpoint open somewhere (like spotifyd or your phone) to receive the command.")

if __name__ == "__main__":
    s = input("Enter the music name to play on Spotify: ")
    play_spotify_music(s)
