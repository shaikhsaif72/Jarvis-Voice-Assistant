# Jarvis - Voice-Activated Virtual Assistant

Jarvis is a voice-activated virtual assistant designed to perform tasks such as opening websites, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model. It listens for the **wake word "Jarvis"** and executes your commands, acting like a simplified version of Alexa or Google Assistant.

---

## Features

- **Voice Recognition:** Converts spoken words into text using the `speech_recognition` library.
- **Wake Word Detection:** Activates upon detecting the wake word "Jarvis."
- **Text-to-Speech:**
  - Converts text to speech using `pyttsx3` for local conversion.
  - Uses `gTTS` (Google Text-to-Speech) and `pygame` for audio playback.
- **Web Browsing:** Opens websites like Google, Facebook, YouTube, and LinkedIn via voice commands.
- **Music Playback:** Interfaces with a `musicLibrary` module to play songs via web links.
- **News Fetching:** Fetches and reads the latest headlines using NewsAPI.
- **OpenAI Integration:** Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.

---

## Project Structure

```
├── main.py           # Main program file (Jarvis logic)
├── musicLibrary.py   # Dictionary of song names and their links
├── client.py         # Sample script to test OpenAI responses independently
├── README.md         # This file
```

---

## Requirements

- Python 3.8 or higher recommended

Install required Python packages before running:

```bash
pip install speechrecognition
pip install pyttsx3
pip install gTTS
pip install pygame
pip install requests
pip install openai
pip install setuptools
pip install pocketsphinx
```

---

## Setup Instructions

1. Clone or download the project folder.
2. Add your favorite songs in `musicLibrary.py`:

```python
music = {
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
}
```

3. Add your API keys:

   - OpenAI API Key: Replace `<Your Key Here>` in `aiProcess()` in `main.py` with your key.
   - NewsAPI API Key: Already added, or you can replace it with your own for reliability.

4. Run the program:

```bash
python main.py
```

5. Say "Jarvis" → Wait for the reply → Give your command.

**Troubleshooting Tip:** If speech recognition doesn’t work, ensure your microphone is properly connected and accessible.

---

## Workflow Summary

1. Initialization → Greets the user with "Initializing Jarvis..."
2. Wake Word Detection → Listens for "Jarvis"
3. Acknowledges activation by saying "Ya."
4. Command Processing → Executes tasks like opening websites, playing music, fetching news, or using OpenAI for responses
5. Speech Output → Provides spoken responses using `gTTS` or `pyttsx3`

---

## Testing OpenAI API (Optional)

A separate script `client.py` is included to test OpenAI's API functionality independently.

Example usage:

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
```

Run it with:

```bash
python client.py
```

---

## Examples of Commands

| Say This                       | What Jarvis Does                      |
| ------------------------------ | ------------------------------------- |
| `Jarvis` → `Open Google`       | Opens google.com in browser           |
| `Jarvis` → `Play faded`        | Plays the YouTube link of "faded"     |
| `Jarvis` → `News`              | Reads out latest headlines (US news)  |
| `Jarvis` → `Who is Elon Musk?` | Gets the answer from OpenAI (ChatGPT) |
| `Jarvis` → `What time is it?`  | Tells the current time                |
| `Jarvis` → `Tell me a joke`    | Responds with a joke from OpenAI      |

---

## To Do / Improvements

- Add error handling for unknown songs
- Add offline speech recognition support
- Implement additional commands (e.g., send email, set reminders, control system volume)
- Create a GUI interface (Tkinter/PyQt)
- Package as `.exe` for Windows using `pyinstaller`

---

## Libraries Used

- speech\_recognition
- webbrowser
- pyttsx3
- musicLibrary (custom)
- requests
- openai
- gTTS
- pygame
- os
- setuptools
- pocketsphinx

---

## Author

Made by **Saif Shaikh** as part of a learning project inspired by CodeWithHarry's Python tutorials.

---

## License

This project is free to use for personal and educational purposes. For commercial use, please contact the author.

