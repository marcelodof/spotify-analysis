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
    spotify.user_playlist_add_tracks(
        user_id,
        playlist_id,
        tracks
    )
    print('These tracks ({}) have been added into the playlist {}'.format(tracks, playlist_id))
