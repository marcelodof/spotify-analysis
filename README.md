# Spotify Analysis
> Repository of exploration analysis of spotify data

Add a credentials file with a `get_credentials` method that returns a dict as:
`{'CLI_ID': '', 'CLI_KEY': ''}`

## spotify_csv_exporter

A script to turn any public playlist in csv files with these headers:

```
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
```

Must create a folder called 'csv'

## exchange_playlist_items

A script that given a array of tracks id, exchange all from a playlist to another

## SpotifyExplorationNotebook

A notebook to explore the csv data returned by the spotify_csv_exporter
