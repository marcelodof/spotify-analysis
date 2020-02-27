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
csv_headers = ["url", "name", "artist", "explicit", "popularity", "duration_ms", "danceability", "energy", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
# whether you want to overwrite existing files or not
OVERWRITE = True


def main():
    global spotify

    # dictionary of playlists with their IDs and owner IDs
    playlists_info = {
        "rock" 					: ["37i9dQZF1DWXRqgorJj26U", "spotify"],
        "hiphop"				: ["37i9dQZF1DX0XUsuxWHRQd", "spotify"],
        "classical"				: ["37i9dQZF1DWWEJlAGA9gs0", "spotify"], 
        "focus"					: ["37i9dQZF1DWZeKCadgRdKQ", "spotify"],
        "edm"					: ["37i9dQZF1DX5Q27plkaOQ3", "spotify"],
        "just"					: ["1MlVgfN4qPrG7cWQLhC4O9", "shivsondhi"],
        "reggaton"				: ["3MQzcmwPwvpy2tdVbqy775", "pcnaimad"]}
    playlist = playlists_info['hiphop']

    #print(CLI_ID)
    # step 1 - get the token to get authorized by the spotify API
    token = get_token()
    spotify = spotipy.Spotify(auth=token)

    # write playlist contents to file and other playlist-operations
    write_playlist(playlist[1], playlist[0])


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


def write_playlist(username, uri):
    '''
    Query the spotify API and receive the playlist information. If mode is 'nan' you can view this information data structure in its raw form.
    Obtain the list of tracks from the playlist information data structure and write it to a txt or csv file.
    Select a random song from the list of tracks and print general information to the console. 
    '''
    playlist_info = spotify.user_playlist(username, uri) 						#, fields='tracks,next,name'
    tracks = playlist_info['tracks']
    filename = "{0}.csv".format(playlist_info['name'])
    old_total = write_csv(filename, tracks)
    print("Number of tracks = {} --> {} ".format(old_total, tracks['total']))


def write_csv(filename, tracks):
    '''
    ADD TO CSV FILE
    View the playlist information data structure if this is confusing! 
    Specify the destination file path and check if the file exists already. If the file exists and you selected to not overwrite, the program will end here.
    Traverse the tracks data structure and add whatever information you want to store to a python list. These are the rows for your csv file
    Append all of these lists to a main python list which will store all the rows for your csv file.
    Write the data to the csv file!
    Exceptions handle the cases where the characters in the track info cannot be understood by the system and where the key is invalid (usually due to local files in the playlist).
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
                    track_url = track['external_urls']['spotify']
                    # add to list of lists
                    track_info = [track_url, track['name'], track['artists'][0]['name'], track['explicit'], track['popularity'], track['duration_ms'], features[0]['danceability'], features[0]['energy'], features[0]['speechiness'], features[0]['acousticness'], features[0]['instrumentalness'], features[0]['liveness'], features[0]['valence'], features[0]['tempo']]
                    tracklist.append(track_info)
                except KeyError:
                    print("Skipping track (LOCAL ONLY) - {0} by {1}".format(track['name'], track['artists'][0]['name']))
        if tracks['next']:
            tracks = spotify.next(tracks)
        else:
            break
    with open(filepath, 'w', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerows(tracklist)
        except UnicodeEncodeError:
            print("Skipping track (UNDEFINED CHARACTERS) - {0} by {1}".format(track['name'], track['artists'][0]['name']))
    print("Playlist written to file.", end="\n\n")
    print("-----\t\t\t-----\t\t\t-----\n")
    return


if __name__ == "__main__":
	main()