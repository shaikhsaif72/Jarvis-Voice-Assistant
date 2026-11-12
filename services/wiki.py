import wikipedia


def wikipedia_search(query):

    try:

        wikipedia.set_lang("en")

        result = wikipedia.summary(
            query,
            sentences=2,
            auto_suggest=True
        )

        return result

    except wikipedia.exceptions.DisambiguationError as e:

        options = ", ".join(e.options[:3])

        return f"There are multiple results. Try {options}."

    except wikipedia.exceptions.PageError:

        return "I couldn't find that topic on Wikipedia."

    except Exception:

        return "Sorry, Wikipedia is unavailable right now."