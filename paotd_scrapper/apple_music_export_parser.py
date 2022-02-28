

if __name__ == "__main__":
    artists = set()
    with open("../AppleMusicLibrary.xml", 'r', encoding='utf-8') as inFile:
        for line in inFile:
            line = line.strip()
            if line.startswith("<key>Artist</key>"):
                line = line.replace("<key>Artist</key>", "")
                line = line.replace("<string>", "")
                line = line.replace("</string>", "")
                artist_name = line.strip()
                artists.add(artist_name)

    artists = list(artists)
    artists.sort()
    with open('artist_list.txt', 'w', encoding='utf-8') as outFile:
        for artist in artists:
            outFile.write(f"{artist}\n")
