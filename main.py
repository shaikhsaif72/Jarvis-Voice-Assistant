
import importlib
import webbrowser
import time


try:
    sr = importlib.import_module("speech_recognition")
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "The SpeechRecognition package is required. "
        "Install it with: pip install SpeechRecognition"
    ) from error

from services.ai import ask_ai
from services.voice import speak
from services.weather import get_weather
from services.news import get_news
from services.search import web_search
from services.wiki import wikipedia_search
from services.music import play_music
from services.system import (
    get_time,
    get_date,
    get_battery,
    open_application,
    close_application,
    lock_computer
)


# =========================
# VOICE RECOGNITION CONFIG
# =========================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5


# =========================
# SPEECH RECOGNITION
# =========================

def listen():
    """Listen to the user's command and convert speech to text."""

    try:

        with sr.Microphone() as source:

            print("Listening...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        command = command.lower().strip()

        print(f"You: {command}")

        return command

    except sr.WaitTimeoutError:

        print("Listening timeout.")
        return ""

    except sr.UnknownValueError:

        print("Could not understand speech.")
        return ""

    except sr.RequestError:

        print("Speech recognition service unavailable.")
        return ""

    except Exception as e:

        print(f"Listening Error: {e}")
        return ""


# =========================
# WEBSITE COMMANDS
# =========================

def open_website(command):

    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "facebook": "https://facebook.com",
        "linkedin": "https://linkedin.com",
        "github": "https://github.com",
        "instagram": "https://instagram.com"
    }

    for name, url in websites.items():

        if f"open {name}" in command:

            webbrowser.open(url)

            speak(f"Opening {name}")

            return True

    return False


# =========================
# SYSTEM COMMANDS
# =========================

def system_command(command):

    # =========================
    # TIME
    # =========================

    time_keywords = [
        "what time is it",
        "what is time",
        "what time it is",
        "what's the time",
        "current time",
        "tell me the time",
        "time"
    ]

    if any(
        keyword in command
        for keyword in time_keywords
    ):

        result = get_time()

        speak(result)

        return True


    # =========================
    # DATE
    # =========================

    date_keywords = [
        "what is today's date",
        "what's today's date",
        "today's date",
        "what date is it",
        "tell me today's date",
        "today date",
        "today"
    ]

    if any(
        keyword in command
        for keyword in date_keywords
    ):

        result = get_date()

        speak(result)

        return True


    # =========================
    # BATTERY
    # =========================

    battery_keywords = [
        "battery",
        "battery level",
        "battery percentage",
        "how much battery",
        "how much charge",
        "battery status"
    ]

    if any(
        keyword in command
        for keyword in battery_keywords
    ):

        result = get_battery()

        speak(result)

        return True


    # =========================
    # OPEN APPLICATIONS
    # =========================

    applications = {
        "chrome": "chrome",
        "vs code": "vs code",
        "vscode": "vscode",
        "notepad": "notepad",
        "calculator": "calculator"
    }

    for name, app in applications.items():

        if (
            f"open {name}" in command
            or f"launch {name}" in command
            or f"start {name}" in command
        ):

            print(
                f"Opening application: {app}"
            )

            success = open_application(app)

            if success:

                speak(
                    f"Opening {name}"
                )

            else:

                speak(
                    f"I couldn't open {name}"
                )

            return True


    # =========================
    # CLOSE APPLICATIONS
    # =========================

    close_applications = {
        "chrome": "chrome",
        "vs code": "vs code",
        "vscode": "vscode",
        "notepad": "notepad",
        "calculator": "calculator"
    }

    for name, app in close_applications.items():

        if (
            f"close {name}" in command
            or f"exit {name}" in command
            or f"quit {name}" in command
            or f"terminate {name}" in command
        ):

            print(
                f"Closing application: {app}"
            )

            success = close_application(app)

            if success:

                speak(
                    f"Closing {name}"
                )

            else:

                speak(
                    f"{name} is not running."
                )

            return True


    # =========================
    # LOCK COMPUTER
    # =========================

    lock_keywords = [
        "lock my computer",
        "lock computer",
        "lock my pc",
        "lock pc"
    ]

    if any(
        keyword in command
        for keyword in lock_keywords
    ):

        speak(
            "Locking your computer."
        )

        success = lock_computer()

        if not success:

            speak(
                "I couldn't lock your computer."
            )

        return True


    return False


# =========================
# WEATHER COMMAND
# =========================

def weather_command(command):

    if "weather" not in command:

        return False

    city = "Mumbai"

    words = command.split()

    if "in" in words:

        index = words.index("in")

        if index + 1 < len(words):

            city = " ".join(
                words[index + 1:]
            )

    print(
        f"Getting weather for {city}..."
    )

    result = get_weather(city)

    speak(result)

    return True


# =========================
# NEWS COMMAND
# =========================

def news_command(command):

    news_keywords = [
        "news",
        "latest news",
        "today's news",
        "top news"
    ]

    if not any(
        keyword in command
        for keyword in news_keywords
    ):

        return False

    print(
        "Getting latest news..."
    )

    result = get_news()

    speak(result)

    return True


# =========================
# WEB SEARCH COMMAND
# =========================

def search_command(command):

    search_triggers = [
        "search for",
        "search",
        "google"
    ]

    for trigger in search_triggers:

        if command.startswith(trigger):

            query = command.replace(
                trigger,
                "",
                1
            ).strip()

            if query:

                print(
                    f"Searching for: {query}"
                )

                web_search(query)

                speak(
                    f"Searching for {query}"
                )

            else:

                speak(
                    "What should I search for?"
                )

            return True

    return False


# =========================
# WIKIPEDIA COMMAND
# =========================

def wiki_command(command):

    triggers = [
        "according to wikipedia",
        "search wikipedia",
        "wikipedia"
    ]

    for trigger in triggers:

        if trigger in command:

            query = command.replace(
                trigger,
                "",
                1
            ).strip()

            if query:

                print(
                    f"Searching Wikipedia for: {query}"
                )

                result = wikipedia_search(
                    query
                )

                speak(result)

            else:

                speak(
                    "What should I search on Wikipedia?"
                )

            return True

    return False


# =========================
# MUSIC COMMAND
# =========================

def music_command(command):

    if not command.startswith("play"):

        return False

    song = command.replace(
        "play",
        "",
        1
    ).strip()

    if not song:

        speak(
            "Which song should I play?"
        )

        return True

    print(
        f"Searching YouTube for: {song}"
    )

    success = play_music(song)

    if success:

        speak(
            f"Searching YouTube for {song}"
        )

    else:

        speak(
            "I couldn't search for that song."
        )

    return True


# =========================
# COMMAND PROCESSING
# =========================

def process_command(command):

    command = command.lower().strip()

    if not command:

        return


    # =========================
    # EXIT / SHUTDOWN
    # =========================

    exit_commands = [
        "bye",
        "goodbye",
        "shutdown",
        "shut down",
        "exit",
        "quit",
        "stop",
        "close jarvis",
        "turn off"
    ]

    if any(
        phrase in command
        for phrase in exit_commands
    ):

        speak("Goodbye.")

        raise SystemExit


    # =========================
    # SYSTEM COMMANDS
    # =========================

    if system_command(command):

        return


    # =========================
    # WEBSITE COMMANDS
    # =========================

    if open_website(command):

        return


    # =========================
    # WEATHER
    # =========================

    if weather_command(command):

        return


    # =========================
    # NEWS
    # =========================

    if news_command(command):

        return


    # =========================
    # WEB SEARCH
    # =========================

    if search_command(command):

        return


    # =========================
    # WIKIPEDIA
    # =========================

    if wiki_command(command):

        return


    # =========================
    # MUSIC
    # =========================

    if music_command(command):

        return


    # =========================
    # AI FALLBACK
    # =========================

    print(
        f"Sending to AI: {command}"
    )

    response = ask_ai(command)

    if response:

        speak(response)


# =========================
# MAIN JARVIS LOOP
# =========================

def main():

    print(
        "\n================================"
    )

    print(
        "       JARVIS AI ASSISTANT"
    )

    print(
        "================================\n"
    )

    speak(
        "Jarvis is starting."
    )


    # =========================
    # MICROPHONE CALIBRATION
    # =========================

    try:

        with sr.Microphone() as source:

            print(
                "Calibrating microphone..."
            )

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print(
                "Microphone ready."
            )

    except Exception as e:

        print(
            f"Microphone Error: {e}"
        )

        speak(
            "Microphone initialization failed."
        )

        return


    speak(
        "I am ready."
    )


    # =========================
    # CONTINUOUS LOOP
    # =========================

    while True:

        try:

            print(
                "\nListening for 'Jarvis'..."
            )

            with sr.Microphone() as source:

                audio = recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=5
                )

            word = recognizer.recognize_google(
                audio,
                language="en-IN"
            ).lower().strip()

            print(
                f"Heard: {word}"
            )


            # =========================
            # WAKE WORD
            # =========================

            if "jarvis" in word:

                command = word.replace(
                    "jarvis",
                    "",
                    1
                ).strip()

                if command:

                    process_command(
                        command
                    )

                else:

                    speak(
                        "Yes?"
                    )

                    time.sleep(
                        0.5
                    )

                    command = listen()

                    if command:

                        process_command(
                            command
                        )


            else:

                # =========================
                # FALLBACK COMMANDS
                # =========================

                command_keywords = [
                    "time",
                    "date",
                    "battery",
                    "weather",
                    "news",
                    "search",
                    "wikipedia",
                    "play",

                    # Open applications
                    "open chrome",
                    "open vs code",
                    "open vscode",
                    "open notepad",
                    "open calculator",

                    # Close applications
                    "close chrome",
                    "close vs code",
                    "close vscode",
                    "close notepad",
                    "close calculator",
                    "exit chrome",
                    "exit vs code",
                    "exit vscode",
                    "exit notepad",
                    "exit calculator",
                    "quit chrome",
                    "quit vs code",
                    "quit vscode",
                    "quit notepad",
                    "quit calculator",

                    # Lock computer
                    "lock my computer",
                    "lock computer",
                    "lock my pc",
                    "lock pc"
                ]

                if any(
                    keyword in word
                    for keyword in command_keywords
                ):

                    process_command(
                        word
                    )

                else:

                    speak(
                        "Yes?"
                    )

                    time.sleep(
                        0.5
                    )

                    command = listen()

                    if command:

                        process_command(
                            command
                        )


        except sr.UnknownValueError:

            continue

        except sr.RequestError:

            print(
                "Speech recognition service unavailable."
            )

        except KeyboardInterrupt:

            print(
                "\nJarvis stopped."
            )

            speak(
                "Goodbye."
            )

            break

        except SystemExit:

            break

        except Exception as e:

            print(
                f"Unexpected Error: {e}"
            )


# =========================
# PROGRAM START
# =========================

if __name__ == "__main__":

    main()
