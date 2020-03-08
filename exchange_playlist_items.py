import utils.playlist_manager as playlist_manager
import spotipy            as spotipy
import spotipy.oauth2     as oauth2
import spotipy.util       as util

tracks = ['1CRFWfZEfLCs7pYDlXFYMJ',
 '2cyTXelFvE7WjSAj8U5vvb',
 '1AhDOtG9vPSOmsWgNW0BEY',
 '5PK1JCSdr34gWgzYHgt3Jq',
 '0YBq701BXkMaK6V5UyvOpT',
 '3FGUAszpLN0pPh2jQL4vOv',
 '3zBvfeQ4RnDfAHQmvLflbk',
 '3DwN8YfAtvJh4c5u8DZPen',
 '1AqJft5Jpmc2ob71KRL562',
 '1cc0kyZrheNxOYPn3VoVEH',
 '3yShr5EC1pAAJcEOKj6h1R',
 '35LwnXpLMRb2kShTHmtPJ5',
 '4yoirlyne2EwkftLG7CpvN',
 '1Fid2jjqsHViMX6xNH70hE',
 '6WXFVBiQCftOIPYcYXNsrM',
 '16i6f7yJWs1j67fxBjfc7z',
 '6FOyzhp375u8DapDyQqGTh',
 '1IycYHHYjKgxvB8AHCdu7O',
 '0GVuLQtPXFaL18ijEOqoAa',
 '0RoA7ObU6phWpqhlC9zH4Z',
 '23L5CiUhw2jV1OIMwthR3S',
 '0L6UCE1Y0KX3MF2AtxlntI',
 '4fDta9k8aRElUr8LalrWQx',
 '2ilm46mO1B10paauIyloxK',
 '7FZz3UM8mkMnUlBTHAPJXp',
 '1LIAdfyn3dtGOyD30Rd5lG',
 '5FiwJejLzaiLzX5iYpPJp9',
 '20NnMHULgUwaFcKBSzb2hN',
 '1ZS7vvlooIov0EFQMQiy3V',
 '1709FMK7A4ZfzXYXyVnFJR',
 '7EUEl5wJb8VI777UAUvRnH',
 '3dglCYsVMjPbDlU2CC9Vq7',
 '3SPcBPzvbmWLl8NU5efx4W',
 '1UmIWsuzcitp1VhsEKviJZ',
 '2aXDWWlbLUapMZnYNDErmv',
 '3fLqmaO4vvZpFZSZy52VMp',
 '36ylLzMtvJ2CItc7bN4TcF',
 '0yb0vfZe6qShIACQJW5GgD',
 '3WVBQjDRoUUTJnWVaUUEHL',
 '3ouugyuxko5bXTKrWSxowx',
 '3o9ZhwPb3TrlgVBcMXffzj',
 '4QIo4oxwzzafcBWkKjDpXY',
 '7CyiXFrHwTOjTbpNy0PlLI',
 '7Jl757vT5eNqemc6PtY2dA',
 '1oke7Jkp9afNQzTUD5iHZZ',
 '51zC0cKP0zSmXgj4kgfbl0',
 '388jD8ko9cvFM9cd9TYDrl',
 '3m1wrL5vw396DIdRqD18mr',
 '4H7WNRErSbONkM06blBoGc',
 '5HhcXOota042Ync4U2OCfc',
 '2zk7TQx9Xa4yxYmsjgDCPp',
 '18wCJcoFmXZ0jfrFhF6cYS',
 '5uJAxWHkaW49n4cXWUP4Xw',
 '6ET9kf9riLETWs9lePUEAI',
 '3bb1W7lUZ4mZwQZAXlPC5d',
 '6tvnj77OJD0DJTgSIi6fQ3',
 '1NEg5LHpn3reJ79r6IY0M6',
 '6fracv4du3sDwo1XKcPrkw',
 '4WxeDb9YZABqk3QaH9CCu1']

def authenticate():
    CLI_ID = '03876df9724646dbbe19742d11ec1b84'
    CLI_KEY = '1e922846e2bf4c7c80cd3acb71692397'
    SCOPE = 'playlist-modify-public'
    REDIRECT_URI = 'http://localhost:8080'

    token = util.prompt_for_user_token('marcelodof',
                                       CLI_ID,
                                       CLI_KEY,
                                       SCOPE,
                                       REDIRECT_URI)

    return spotipy.Spotify(auth=token)

def main():
    spotify = authenticate()

    user_id = 'marcelodof'
    playlist_id_dizem = '7bq3dy7YjKcTDvd4DrLMzN'
    playlist_id_tristeza = '66StSH0fC8xwrAy6jStQSD'
    playlist_manager.remove_tracks_from_playlist(spotify, user_id, tracks, playlist_id_dizem)
    playlist_manager.add_tracks_in_playlist(spotify, user_id, tracks, playlist_id_tristeza)

if __name__ == "__main__":
	main()