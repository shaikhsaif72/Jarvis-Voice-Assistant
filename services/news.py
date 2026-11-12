import requests

from config import NEWS_API_KEY


def clean_headline(title):

    if not title:
        return ""

    return title.strip()

def get_news():

    if not NEWS_API_KEY:
        return "News API key is not configured."

    try:

        url = "https://newsdata.io/api/1/latest"

        params = {
            "apikey": NEWS_API_KEY,
            "country": "in",
            "language": "en",
            "size": 5
        }

        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        data = response.json()

        if response.status_code != 200:

            print(f"News API Error: {data}")

            return "I couldn't fetch the latest news."

        articles = data.get("results", [])

        if not articles:

            return "I couldn't find any latest news."

        headlines = []

        for article in articles:

            title = article.get("title")

            title = clean_headline(title)

            if title:

                headlines.append(title)

            if len(headlines) == 5:

                break

        if not headlines:

            return "I couldn't find any readable news."

        # =========================
        # FORMAT NEWS
        # =========================

        news_text = "Here are today's top news updates.\n\n"

        for index, headline in enumerate(
            headlines,
            start=1
        ):

            news_text += (
                f"News {index}: {headline}\n\n"
            )

        return news_text.strip()

    except requests.RequestException:

        return (
            "The news service is currently "
            "unavailable."
        )

    except Exception as e:

        print(f"News Error: {e}")

        return (
            "Sorry, I couldn't fetch the "
            "latest news."
        )