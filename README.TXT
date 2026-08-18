# 🤖 Jarvis – Voice Assistant Using Python

A Python-based **voice-controlled personal assistant** inspired by the fictional AI assistant **JARVIS**. The assistant listens to voice commands, responds using text-to-speech, searches Wikipedia, opens websites, plays music, and can display saved Wi-Fi profiles on a Windows system.

## 🚀 Features

* 🎙️ **Voice Recognition** – Converts spoken commands into text using Google Speech Recognition.
* 🔊 **Text-to-Speech** – Responds to the user using `pyttsx3`.
* 📚 **Wikipedia Search** – Retrieves brief information directly from Wikipedia.
* 🌐 **Website Automation** – Opens Google, YouTube, and Stack Overflow through voice commands.
* 🎵 **Music Player** – Randomly selects and plays a song from the configured music directory.
* 📶 **Saved Wi-Fi Profile Viewer** – Uses Windows `netsh` commands to display Wi-Fi profiles saved on the computer.
* 👋 **Voice Greeting** – Provides different greetings depending on the time of day.
* 🛑 **Voice Exit Command** – Allows the user to close the assistant using a voice command.

## 🛠️ Technologies Used

* **Python**
* `SpeechRecognition`
* `PyAudio`
* `pyttsx3`
* `Wikipedia API`
* `datetime`
* `subprocess`
* `webbrowser`
* `os`
* `random`
* `re`

## 📂 Project Structure

```text
Jarvis-Voice-Assistant/
│
├── jarvis.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```

### 2. Install the required libraries

```bash
pip install pyttsx3 SpeechRecognition wikipedia PyAudio
```

> **Note:** `PyAudio` may require additional installation steps on some Windows systems.

### 3. Configure the Music Directory

Open the Python file and update:

```python
MUSIC_DIR = r"C:\Users\YourName\Music"
```

Replace the path with the location of your music folder.

### 4. Run the Assistant

```bash
python jarvis.py
```

Make sure your **microphone is connected and accessible** before starting the program.

## 🎤 Supported Voice Commands

| Voice Command         | Action                          |
| --------------------- | ------------------------------- |
| `Open Google`         | Opens Google                    |
| `Open YouTube`        | Opens YouTube                   |
| `Open Stack Overflow` | Opens Stack Overflow            |
| `Play Music`          | Plays a random song             |
| `Wikipedia <topic>`   | Searches Wikipedia              |
| `Who is your founder` | Displays the configured founder |
| `WiFi Passwords`      | Shows saved Wi-Fi profiles      |
| `Exit`                | Closes Jarvis                   |

### Example

Say:

```text
"Open YouTube"
```

Jarvis will respond:

```text
"Opening YouTube"
```

and open YouTube in the default web browser.

## 🔐 Wi-Fi Feature & Security Note

The Wi-Fi functionality uses the Windows built-in:

```text
netsh wlan
```

commands to inspect **Wi-Fi profiles already saved on the local Windows computer**.

It does **not** crack passwords, attack wireless networks, or retrieve credentials from networks the computer has never connected to.

Use this feature only on systems and accounts you are authorized to access.

## 🧠 How It Works

The application follows a simple voice-assistant workflow:

```text
User speaks
     ↓
Microphone captures audio
     ↓
Speech Recognition converts audio → text
     ↓
Command is processed
     ↓
Appropriate function is executed
     ↓
Jarvis responds using Text-to-Speech
```

## 📌 Important Notes

* This project is primarily designed for **Windows**.
* Internet access is required for Google Speech Recognition and Wikipedia searches.
* The `MUSIC_DIR` path must be changed according to your computer.
* The `netsh` Wi-Fi functionality depends on Windows networking commands.
* A working microphone is required for voice commands.

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add weather information
* [ ] Add real-time news search
* [ ] Add reminders and alarms
* [ ] Add calculator functionality
* [ ] Add system information commands
* [ ] Add application launching
* [ ] Add AI-powered conversational responses
* [ ] Add a graphical user interface
* [ ] Add configurable voice commands
* [ ] Improve error handling and command recognition

## 👨‍💻 Author

Siddhant Sengar

A Python-based project created to explore **voice recognition, automation, speech synthesis, and system interaction**.

## ⭐ Contributing

Contributions and suggestions are welcome. Feel free to fork this repository, improve the project, and submit a pull request.

## 📄 License

This project is intended for educational and personal use.
