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
from credentials import get_credentials
import random
from pprint import pprint
import csv
import os

# Header row for csv file 
csv_headers = ["id",
               "url", 
               "name",
               "artist",
               "album",
               "explicit",
               "popularity",
               "duration_ms",
               "key",
               "mode",
               "time_signature",
               "danceability",
               "energy",
               "speechiness",
               "acousticness",
               "instrumentalness",
               "liveness",
               "valence",
               "tempo"
               ]
# Whether you want to overwrite existing files or not
OVERWRITE = True

def format_name(name):
    temp = name.lower()
    temp = temp.replace(' ', '_')
    return temp

class SpotifyPlaylist2CSV:
    """SpotifyPlaylist2CSV Class."""
    def __init__(self, config):
        credentials = oauth2.SpotifyClientCredentials(
            client_id = config['CLI_ID'], 
            client_secret = config['CLI_KEY'])
        token = credentials.get_access_token()
        spotify = spotipy.Spotify(auth=token)
        self.spotify = spotify
    
    def choose_playlists(self):
        """Print info of user playlists and 
        let it choose which to print in CSV."""
        user = input('Input spotifys username: ')
        results = self.spotify.user_playlists(user)
        playlists = []
        i = 1
        print('\n')
        for item in results['items']:
            new_item = {}
            new_item['user'] = user
            new_item['id'] = item['id']
            new_item['name'] = format_name(item['name'])
            playlists.append(new_item)
            print('{}: {}'.format(i, new_item['name']))
            i = i + 1

        print('\n')
        index = input('Choose playlist: ')
        print('\n')
        self.playlist = playlists[int(index) - 1]


    
    def write_playlist(self):
        '''
        Query the spotify API and receive the playlist information.
        Obtain the list of tracks from the playlist information data structure 
        and write it to a txt or csv file.
        '''
        print("Writting playlist {} into csv.".format(self.playlist['name']))
        playlist_info = self.spotify.user_playlist(self.playlist['user'], self.playlist['id'])
        self.tracks = playlist_info['tracks']
        self.write_csv()
        print("Number of tracks = {} ".format(self.tracks['total']))

    def write_csv(self):
        '''
        Write the data to the csv file.
        View the playlist information data structure if this is confusing! 
        Specify the destination file path and check if the file exists already. 
        If the file exists and you selected to not overwrite,
        Exceptions handle the cases where the characters in the track info 
        cannot be understood by the system and where the key is invalid 
        (usually due to local files in the playlist).
        '''
        filepath = "./csv/{0}".format("{0}.csv".format(self.playlist['name']))
        tracklist = []
        tracklist.append(csv_headers)
        if os.path.isfile(filepath):
            print("File already exists!")
            if not OVERWRITE:
                return
            else:
                print("Rewriting...")
        while True:
            for item in self.tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                if track != None:
                    try:
                        features = self.spotify.audio_features([track['id']])
                        track_info = [track['id'],
                                    track['external_urls']['spotify'],
                                    track['name'],
                                    track['artists'][0]['name'],
                                    track['album']['name'],
                                    track['explicit'],
                                    track['popularity'],
                                    track['duration_ms'],
                                    features[0]['key'],
                                    features[0]['mode'],
                                    features[0]['time_signature'],
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
            if self.tracks['next']:
                self.tracks = self.spotify.next(self.tracks)
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

def main():
    """Main entry point."""
    config = get_credentials()
    Spo = SpotifyPlaylist2CSV(config)
    Spo.choose_playlists()
    Spo.write_playlist()

if __name__ == "__main__":
	main()