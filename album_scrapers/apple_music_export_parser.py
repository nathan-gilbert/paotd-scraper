

def parse_apple_music_artist_xml():
    artists = set()
    with open("../AppleMusicLibrary.xml", 'r', encoding='utf-8') as in_file:
        for line in in_file:
            line = line.strip()
            if line.startswith("<key>Artist</key>"):
                line = line.replace("<key>Artist</key>", "")
                line = line.replace("<string>", "")
                line = line.replace("</string>", "")
                artist_name = line.strip()
                artists.add(artist_name)

    artists = list(artists)
    artists.sort()
    with open('artist_list.txt', 'w', encoding='utf-8') as out_file:
        for artist in artists:
            out_file.write(f"{artist}\n")
