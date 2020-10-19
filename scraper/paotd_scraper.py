import wikipedia


def is_album(text):
    album_words = ["album", "lp", "record"]
    if any(x in text for x in album_words):
        return True
    return False


def get_release_date(text):
    released = text.find("released")
    return released


if __name__ == "__main__":
    with open('../artist_list.txt', 'r') as artist_file:
        for artist in artist_file:
            if artist.startswith("#"):
                continue
            artist = artist.strip()
            print(f"{artist} ...")
            discography = wikipedia.page(f"{artist}_discography")
            for link in discography.links:
                link_page = wikipedia.page(link)
                link_content = link_page.content[:200]
                if is_album(link_content.lower()):
                    print(link_page.title)

                    date_str = get_release_date(link_page.content)
            # print(discography.content)
            # print(discography.links)
            print("end.")
