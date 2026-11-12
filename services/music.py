import webbrowser
from urllib.parse import quote


def play_music(song):

    if not song:
        return False

    query = quote(song)

    url = (
        f"https://www.youtube.com/results?search_query={query}"
    )

    webbrowser.open(url)

    return True