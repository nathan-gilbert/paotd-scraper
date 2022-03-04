from typing import List
import pickle

from dotenv import dotenv_values
import applemusicpy

from music_data.artist import Artist
from music_data.album import Album

config = dotenv_values("../.env")
secret_key = config["APPLE_MUSIC_KEY"]
key_id = config["APPLE_MUSIC_KEY_ID"]
team_id = config["APPLE_MUSIC_TEAM_ID"]


def read_artist_list() -> List[str]:
    with open('../artist_list.txt', 'r', encoding='utf-8') as inFile:
        return list(map(lambda x: x.strip(), inFile.readlines()))


def get_artist_ids(artist_list: List[str]) -> List[Artist]:
    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    artist_objs: List[Artist] = []
    for artist_name in artist_list:
        results = am.search(artist_name, types=['artists'], limit=1)
        if 'artists' in results['results']:
            for item in results['results']['artists']['data']:
                artist_objs.append(Artist(name=artist_name, id=item['id']))
        else:
            print(f"No results for {artist_name}")
    return artist_objs


def get_artist_albums(artist_id: str) -> List[Album]:
    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    results = am.artist_relationship(artist_id, relationship='albums')

    albums: List[Album] = []
    for item in results['data']:
        album_id = item['id']
        album_name = item['attributes']['name']
        album_release_date = item['attributes']['releaseDate']
        album_artist = item['attributes']['artistName']
        is_single = item['attributes']['isSingle']
        is_compilation = item['attributes']['isCompilation']
        albums.append(
            Album(id=album_id,
                  artist=album_artist,
                  name=album_name,
                  releaseDate=album_release_date,
                  isSingle=is_single,
                  isCompilation=is_compilation))
    return albums


def export_to_file(albums: List[Album]):
    with open("all_albums.pkl", "wb") as outFile:
        pickle.dump(albums, outFile)


if __name__ == "__main__":
    artist_names = read_artist_list()
    artists = get_artist_ids(artist_names)
    all_albums: List[Album] = []
    for artist in artists:
        all_albums.extend(get_artist_albums(artist.id))

    for album in all_albums:
        print(album)
    print(f"{len(all_albums)} total albums")

    export_to_file(all_albums)
