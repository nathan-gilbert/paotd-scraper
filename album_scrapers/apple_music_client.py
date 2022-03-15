import pickle
import datetime
from typing import List


from music_data.artist import Artist
from music_data.album import Album


def read_artist_list(artist_file: str) -> List[str]:
    with open(artist_file, 'r', encoding='utf-8') as in_file:
        return list(map(lambda x: x.strip(), in_file.readlines()))


def get_artist_ids(am, artist_list: List[str]) -> List[Artist]:
    artist_objs: List[Artist] = []
    for artist_name in artist_list:
        if artist_name.startswith("#") or artist_name == "":
            continue

        results = am.search(artist_name, types=['artists'], limit=1)
        if 'artists' in results['results']:
            for item in results['results']['artists']['data']:
                artist_objs.append(Artist(name=artist_name, id=item['id']))
        else:
            print(f"No results for {artist_name}")
    return artist_objs


def get_artist_albums(am, artist_id: str) -> List[Album]:
    results = am.artist_relationship(artist_id, relationship='albums')

    albums: List[Album] = []
    for item in results['data']:
        album_id = item['id']
        album_name = item['attributes']['name']
        album_release_date_str = item['attributes']['releaseDate']
        print(album_release_date_str)
        try:
            album_release_date = datetime.datetime.strptime(
                album_release_date_str, "%Y-%m-%d")
        except ValueError:
            try:
                album_release_date = datetime.datetime.strptime(
                    album_release_date_str, "%Y-%m")
                #print(f"Incomplete release date found for {album_name} of "
                #      f"{album_release_date_str}")
            except ValueError:
                #print(f"Incomplete release date found for {album_name} of "
                #      f"{album_release_date_str}")
                continue

        album_artist = item['attributes']['artistName']
        is_single = item['attributes']['isSingle']
        is_compilation = item['attributes']['isCompilation']
        albums.append(
            Album(id=album_id,
                  artist=album_artist,
                  name=album_name,
                  release_date=album_release_date.strftime("%m/%d/%Y"),
                  is_single=is_single,
                  is_compilation=is_compilation))
    return albums


def export_to_pickle(albums: List[Album]):
    with open("all_albums.pkl", "wb") as out_file:
        pickle.dump(albums, out_file)
