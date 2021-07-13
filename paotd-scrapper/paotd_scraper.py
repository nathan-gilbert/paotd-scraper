import wikipedia
import datefinder


def is_album(text):
    album_words = ["album", "lp", "record"]
    if any(x in text for x in album_words):
        return True
    return False


def get_release_date(text):
    matches = datefinder.find_dates(text)
    first_match = ""
    for match in matches:
        first_match = match.strftime('%m-%d-%Y')
        break

    return first_match


if __name__ == "__main__":
    with open('../artist_list.txt', 'r') as artist_file:
        for artist in artist_file:
            if artist.startswith("#"):
                continue
            artist = artist.strip()
            print(f"{artist} ...")
            discography = wikipedia.page(f"{artist}_discography")
            for link in discography.links:
                try:
                    link_page = wikipedia.page(link)
                except wikipedia.exceptions.PageError:
                    continue
                link_content = link_page.content[:200]
                if is_album(link_content.lower()):
                    date_str = get_release_date(link_page.content)
                    print(f"{link_page.title} : {date_str}")
            # print(discography.content)
            # print(discography.links)
            print("end.")
