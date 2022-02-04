import applemusicpy
from dotenv import dotenv_values

config = dotenv_values("../.env")
secret_key = config["APPLE_MUSIC_KEY"]
key_id = config["APPLE_MUSIC_KEY_ID"]
team_id = config["APPLE_MUSIC_TEAM_ID"]


def get_albums():
    am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
    results = am.search('pink floyd', types=['albums'])

    for item in results['results']['albums']['data']:
        print(item['attributes']['name'])


if __name__ == "__main__":
    get_albums()
