from typing import List
from music_data.album import Album
from album_scrapers.csv_exporter import export_albums_to_csv
from album_scrapers.apple_music_client import read_artist_list, \
    get_artist_ids, get_artist_albums

if __name__ == "__main__":
    artist_names = read_artist_list()
    artists = get_artist_ids(artist_names)
    all_albums: List[Album] = []
    for artist in artists:
        all_albums.extend(get_artist_albums(artist.id))

    for album in all_albums:
        print(album)
    print(f"{len(all_albums)} total albums")

    export_albums_to_csv(all_albums)
