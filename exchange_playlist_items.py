import utils.playlist_manager as playlist_manager
from credentials import get_credentials
import spotipy            as spotipy
import spotipy.oauth2     as oauth2
import spotipy.util       as util

tracks = []
from_playlist = ''
to_playlist = ''
user_id = ''

def authenticate():

    credentials = get_credentials()
    SCOPE = 'playlist-modify-public user-library-read'
    REDIRECT_URI = 'http://localhost:8888/callback'

    token = util.prompt_for_user_token(user_id,
                                       SCOPE,
                                       credentials['CLI_ID'],
                                       credentials['CLI_KEY'],
                                       REDIRECT_URI)
    
    return spotipy.Spotify(auth=token)

def main():
    spotify = authenticate()

    playlist_manager.remove_tracks_from_playlist(spotify, user_id, tracks, from_playlist)
    playlist_manager.add_tracks_in_playlist(spotify, user_id, tracks, to_playlist)

if __name__ == "__main__":
	main()