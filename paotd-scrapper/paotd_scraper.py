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



