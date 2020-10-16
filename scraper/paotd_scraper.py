import wikipedia


if __name__ == "__main__":
    with open('../artist_list.txt', 'r') as artistFile:
        for artist in artistFile:
            if artist.startswith("#"):
                continue
            artist = artist.strip()
            print(f"{artist} ...")
            discography = wikipedia.page(f"{artist}_discography")
            print(discography.title)
            print("done.")
            # print(discography.content)
            # print(discography.links)
