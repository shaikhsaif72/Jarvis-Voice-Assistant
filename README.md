# Jarvis Voice Assistant 🎙️🤖

An AI-powered desktop voice assistant built with Python that can understand voice commands, answer questions using Google's Gemini AI, fetch live information, and perform basic Windows system operations.

Jarvis is designed to make everyday desktop interactions easier through voice-controlled automation and AI-powered assistance.

## ✨ Features

### 🎙️ Voice Interaction
- Speech recognition using SpeechRecognition.
- Text-to-speech responses using pyttsx3.
- Wake-word activation using "Jarvis".
- Continuous voice listening.
- Support for Indian English (`en-IN`).
- Microphone calibration for better recognition.

### 🤖 AI-Powered Conversations
- Google Gemini API integration.
- Answers general questions and performs basic conversational tasks.
- Short, voice-friendly AI responses.
- Error handling for API failures and unavailable services.

### 🌐 Web & Information Services
- Open popular websites:
  - Google
  - YouTube
  - Facebook
  - LinkedIn
  - GitHub
  - Instagram
- Google search through voice commands.
- Wikipedia search and summaries.
- Latest Indian news headlines using NewsData.io.
- Real-time weather information using Open-Meteo.

### 🎵 Music Search
- Search songs directly on YouTube using voice commands.
- No manually maintained song URL list required.

### 💻 Windows System Automation
- Get current time and date.
- Check battery percentage and charging status.
- Open applications:
  - Google Chrome
  - Visual Studio Code
  - Notepad
  - Calculator
- Close supported applications using Windows process management.
- Lock the computer through voice commands.
- Safely exit the Jarvis assistant.

### 🔐 Security
- API keys stored in environment variables.
- `.env` excluded from Git using `.gitignore`.
- `.env.example` provided for configuration reference.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Voice input and speech recognition |
| PyAudio | Microphone input |
| pyttsx3 | Text-to-speech |
| Google Gemini API | AI-powered responses |
| Requests | API communication |
| NewsData.io | Latest news |
| Open-Meteo | Weather information |
| Wikipedia | Knowledge search |
| Webbrowser | Website and YouTube search |
| psutil | Battery information |
| Windows subprocess | Application management |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```text
Jarvis-Voice-Assistant/
│
├── main.py
├── config.py
├── musicLibrary.py
│
├── services/
│   ├── ai.py
│   ├── voice.py
│   ├── weather.py
│   ├── news.py
│   ├── search.py
│   ├── wiki.py
│   └── music.py
│   └── system.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

*Note: `musicLibrary.py` is part of the existing repository and is currently not used by the YouTube music search service.*

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shaikhsaif72/Jarvis-Voice-Assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd Jarvis-Voice-Assistant
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** PyAudio may require additional setup depending on your Windows and Python environment.

### 5. Configure Environment Variables

Create a `.env` file in the root directory.

Add the following:

```env
AI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsdata_api_key
```

Get your API keys:

- Gemini API: https://aistudio.google.com/
- NewsData.io: https://newsdata.io/

Weather functionality uses Open-Meteo and does not require an API key.

**Important:** Never upload your `.env` file or expose your API keys publicly.

### 6. Run Jarvis

```bash
python main.py
```

---

## 🗣️ Voice Commands

| Category | Example Commands |
|---|---|
| Wake Word | "Jarvis" |
| AI Assistant | "Jarvis, explain machine learning" |
| Website | "Jarvis, open YouTube" |
| Google Search | "Jarvis, search Python tutorials" |
| Wikipedia | "Jarvis, search Wikipedia for artificial intelligence" |
| Weather | "Jarvis, what's the weather in Mumbai?" |
| News | "Jarvis, tell me the latest news" |
| Music | "Jarvis, play Tum Hi Ho" |
| Time | "Jarvis, what time is it?" |
| Date | "Jarvis, what's today's date?" |
| Battery | "Jarvis, check battery status" |
| Open Application | "Jarvis, open calculator" |
| Close Application | "Jarvis, close notepad" |
| Lock Computer | "Jarvis, lock my computer" |
| Exit Assistant | "Jarvis, shutdown" |

Commands can also be recognized without the wake word in supported fallback scenarios.

---

## 🧠 Project Architecture

The project uses a modular service-based approach.

- `main.py` – Main execution loop, wake-word detection and command routing.
- `config.py` – Loads environment variables and API configuration.
- `services/ai.py` – Gemini AI integration.
- `services/voice.py` – Text-to-speech functionality.
- `services/weather.py` – Weather data retrieval.
- `services/news.py` – Latest news retrieval.
- `services/search.py` – Google search functionality.
- `services/wiki.py` – Wikipedia integration.
- `services/music.py` – YouTube music search.
- `services/system.py` – Windows system operations.

This separation makes the project easier to maintain and extend.

---

## 🚀 Development Roadmap

The project will be upgraded in three development phases.

### Phase 1 – Core Assistant Expansion
- Fix command fallback and improve command detection.
- Integrate calendar functionality.
- Add more Windows system controls.
- Expand application control.

### Phase 2 – Smart Assistant
- File and folder management.
- Improve AI architecture.
- Add conversational memory and context.
- Implement logging and activity tracking.

### Phase 3 – Production & Portfolio Polish
- Centralized configuration management.
- Robust error handling and offline resilience.
- Improved project architecture.
- Professional documentation, screenshots, demo and GitHub presentation.

---

## 🎯 Project Goal

The goal is to evolve Jarvis from a basic Python voice assistant into a modular, AI-powered desktop automation system with intelligent conversations, real-time information retrieval and practical Windows system control.

## 👨‍💻 Author

**Saif Shaikh**

- GitHub: https://github.com/shaikhsaif72

---

⭐ If you find this project interesting, consider giving it a star!
