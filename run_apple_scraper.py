from typing import List
from dotenv import dotenv_values
import applemusicpy

from music_data.album import Album
from album_scrapers.csv_exporter import export_albums_to_csv
from album_scrapers.apple_music_client import read_artist_list, \
    get_artist_ids, get_artist_albums

config = dotenv_values(".env")
secret_key = config["APPLE_MUSIC_KEY"]
key_id = config["APPLE_MUSIC_KEY_ID"]
team_id = config["APPLE_MUSIC_TEAM_ID"]

if __name__ == "__main__":
    artist_names = read_artist_list("artist_list.txt")

    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    artists = get_artist_ids(am, artist_names)
    all_albums: List[Album] = []
    for artist in artists:
        all_albums.extend(get_artist_albums(am, artist.id))

    # for album in all_albums:
    #    print(album)
    print(f"{len(all_albums)} total albums")

    export_albums_to_csv(all_albums)
