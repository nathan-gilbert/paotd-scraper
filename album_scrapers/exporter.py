import csv
from typing import List
from music_data.album import Album


def export_albums_to_csv(albums: List[Album]):
    with open('albums.csv', 'wb') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        for album in albums:
            wr.writerow(list(album))
