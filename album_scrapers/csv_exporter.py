import csv
from typing import List
from music_data.album import Album


def export_albums_to_csv(albums: List[Album]):
    headers = ["id", "artist", "name", "release_date", "is_single",
               "is_compilation"]
    with open('albums.csv', 'w', encoding="utf-8") as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(headers)
        wr.writerows(albums)
