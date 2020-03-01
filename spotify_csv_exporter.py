'''
Using Spotipy to make calls to the Spotify Web API. 
Control variables - [All are either global or in main()]
	* CLI_ID and CLI_KEY	(string)
	* overwrite 			(boolean)
	* mode 					(string)
	* playlist 				(list of strings)
'''

import spotipy
import spotipy.oauth2 as oauth2
import random
from pprint import pprint
import csv
import os


# client ID and secret key to authorize querying of spotify data through the API
CLI_ID 	= ''
CLI_KEY = ''

# header row for csv file 
csv_headers = ["id",
               "url", 
               "name",
               "artist",
               "explicit",
               "popularity",
               "duration_ms",
               "danceability",
               "energy",
               "speechiness",
               "acousticness",
               "instrumentalness",
               "liveness",
               "valence",
               "tempo"
               ]
# whether you want to overwrite existing files or not
OVERWRITE = True


def main():
    global spotify

    playlists_info = [
        ["dizem_que_o_amor_atrai", "marcelodof", "7bq3dy7YjKcTDvd4DrLMzN"],
        ["a_tristeza_e_senhora", "marcelodof", "66StSH0fC8xwrAy6jStQSD"]
    ]

    token = get_token()
    spotify = spotipy.Spotify(auth=token)

    # Choose your playlist here
    playlist = playlists_info[1]

    write_playlist(playlist[0], playlist[1], playlist[2])


def get_token():
    '''
    Your client ID and client secret key are used to get a token. 
    If both your credentials were legitimate, you will get and return a valid token. 
    '''
    credentials = oauth2.SpotifyClientCredentials(
        client_id = CLI_ID, 
        client_secret = CLI_KEY)
    token = credentials.get_access_token()
    return token 


def write_playlist(playlistname, username, uri):
    '''
    Query the spotify API and receive the playlist information.
    Obtain the list of tracks from the playlist information data structure 
    and write it to a txt or csv file.
    '''
    print("Writting playlist {} into csv.".format(playlistname))
    playlist_info = spotify.user_playlist(username, uri)
    tracks = playlist_info['tracks']
    filename = "{0}.csv".format(playlistname)
    write_csv(filename, tracks)
    print("Number of tracks = {} ".format(tracks['total']))


def write_csv(filename, tracks):
    '''
    Write the data to the csv file.
    View the playlist information data structure if this is confusing! 
    Specify the destination file path and check if the file exists already. 
    If the file exists and you selected to not overwrite,
    Exceptions handle the cases where the characters in the track info 
    cannot be understood by the system and where the key is invalid 
    (usually due to local files in the playlist).
    '''
    filepath = "./csv/{0}".format(filename)
    tracklist = []
    tracklist.append(csv_headers)
    if os.path.isfile(filepath):
        print("File already exists!")
        if not OVERWRITE:
            return
        else:
            print("Rewriting...")
    while True:
        for item in tracks['items']:
            if 'track' in item:
                track = item['track']
            else:
                track = item
            if track != None:
                try:
                    features = spotify.audio_features([track['id']])
                    track_info = [track['id'],
                                 track['external_urls']['spotify'],
                                 track['name'],
                                 track['artists'][0]['name'],
                                 track['explicit'],
                                 track['popularity'],
                                 track['duration_ms'],
                                 features[0]['danceability'],
                                 features[0]['energy'],
                                 features[0]['speechiness'],
                                 features[0]['acousticness'],
                                 features[0]['instrumentalness'],
                                 features[0]['liveness'],
                                 features[0]['valence'],
                                 features[0]['tempo']
                                ]
                    tracklist.append(track_info)
                except KeyError:
                    print("Skipping track - {0} by {1}".format(track['name'], track['artists'][0]['name']))
        if tracks['next']:
            tracks = spotify.next(tracks)
        else:
            break
    with open(filepath, 'w', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerows(tracklist)
        except UnicodeEncodeError:
            print("Skipping track - {0} by {1}".format(track['name'], track['artists'][0]['name']))
    print("Playlist written to file.", end="\n\n")
    return


if __name__ == "__main__":
	main()