import utils.playlist_manager as playlist_manager
import time
from credentials import get_credentials
import pandas             as pd
import spotipy            as spotipy
import spotipy.oauth2     as oauth2
import spotipy.util       as util

user_id = 'marcelodof'

def authenticate():

    credentials = get_credentials()
    SCOPE = 'playlist-modify-public'
    REDIRECT_URI = 'http://localhost:8888/callback'

    token = util.prompt_for_user_token(user_id,
                                       SCOPE,
                                       credentials['CLI_ID'],
                                       credentials['CLI_KEY'],
                                       REDIRECT_URI)
    
    return spotipy.Spotify(auth=token)

def main():

    spotify = authenticate()
    df = pd.read_csv('csv/cluster_zero_tracks.csv')
    tracks = df['id'].tolist()

    playlist_manager.create_playlist(
        spotify,
        user_id,
        'pl4l1st g3n3r4t0r - Cluster 0',
        True,
        'Clusterization Method: KMeans - \
            Playlist generated at {}'.format(time.strftime('%c')),
        tracks
    )

if __name__ == "__main__":
	main()