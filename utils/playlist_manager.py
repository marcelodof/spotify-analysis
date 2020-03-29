"""Playlist functions."""

def remove_tracks_from_playlist(spotify, user_id, tracks, playlist_id):
    """Remove a list of tracks id from a given playlist."""
    spotify.user_playlist_remove_all_occurrences_of_tracks(
        user_id,
        playlist_id,
        tracks
    )
    print('These tracks ({}) have been removed from the playlist {}'.format(tracks, playlist_id))

def add_tracks_in_playlist(spotify, user_id, tracks, playlist_id):
    """Add a list of tracks id in a given playlist."""
    batch_num = 100
    if len(tracks) > batch_num:
        for i in range(0, len(tracks), batch_num):
            spotify.user_playlist_add_tracks(
                user_id,
                playlist_id,
                tracks[(i):(batch_num + i)]
            )
            print('Inserted from {0} to {1}'.format(i, batch_num+i))
    else:
        spotify.user_playlist_add_tracks(
            user_id,
            playlist_id,
            tracks
        )
    print('{} tracks have been added into the playlist {}'.format(len(tracks), playlist_id))

def create_playlist(spotify, user_id, playlist_name, is_public, playlist_description, tracks=None):
    playlist_info = spotify.user_playlist_create(
        user_id,
        playlist_name,
        is_public,
        playlist_description
    )
    if tracks == None:
        return
    else:
        add_tracks_in_playlist(spotify, user_id, tracks, playlist_info['id'])
