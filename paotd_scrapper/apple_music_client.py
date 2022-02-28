from typing import List, Dict, Tuple
from dotenv import dotenv_values
import applemusicpy

config = dotenv_values("../.env")
secret_key = config["APPLE_MUSIC_KEY"]
key_id = config["APPLE_MUSIC_KEY_ID"]
team_id = config["APPLE_MUSIC_TEAM_ID"]


def read_artist_list() -> List[str]:
    with open('../artist_list.txt', 'r', encoding='utf-8') as inFile:
        return list(map(lambda x: x.strip(), inFile.readlines()))


def get_artist_ids(artist_list: List[str]) -> Dict[str, str]:
    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    artist_map = {}
    for artist_name in artist_list:
        results = am.search(artist_name, types=['artists'], limit=1)
        for item in results['results']['artists']['data']:
            artist_map[artist_name] = item['id']
    return artist_map


def get_artist_albums(artist_id: str) -> List[Tuple[str, str]]:
    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    results = am.artist_relationship(artist_id, relationship='albums')

    albums = []
    for item in results['results']['albums']['data']:
        print(item['attributes']['name'], item['attributes']['releaseDate'])

    return albums


if __name__ == "__main__":
    artists = read_artist_list()
    artist_ids = get_artist_ids(artists)
    for artist in artists:
        artist_albums = get_artist_albums(artist_ids[artist])
