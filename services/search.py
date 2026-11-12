import webbrowser
from urllib.parse import quote


def web_search(query):

    if not query:
        return False

    url = f"https://www.google.com/search?q={quote(query)}"

    webbrowser.open(url)

    return True