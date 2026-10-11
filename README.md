# 🤖 ChipChap AI

A friendly desktop chat assistant built with Python and **CustomTkinter**.
You can switch between two AI backends, **OpenAI** (cloud) and **Ollama** (local), straight from the app.

---

## ✨ Features

- **Hybrid AI backend:** switch between OpenAI `gpt-4o-mini` and a local Ollama `llama3` model from a dropdown menu
- **Modern chat UI:** message bubbles, a scrollable chat window and a rounded input field, built with CustomTkinter
- **Responsive while thinking:** AI requests run in a background thread, so the window never freezes
- **Animated "thinking" indicator** (`● ○ ○`) while the answer is on its way
- **Session memory:** ChipChap remembers the conversation while the app is open and forgets it when you close it
- **Answers in your language:** it detects the language you write in and replies in the same one
- **Keyboard friendly:** press **Enter** to send a message

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) | Desktop GUI |
| [OpenAI Python SDK](https://github.com/openai/openai-python) | Cloud AI (`gpt-4o-mini`) |
| [Ollama](https://ollama.com/) | Local AI (`llama3`) |
| python-dotenv | Loads the API key from a `.env` file |
| threading | Keeps the UI responsive |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/chipchap.git
cd chipchap
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Copy `.env.example` to `.env` and paste in your key:

```
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. (Optional) Set up Ollama for local AI

Install [Ollama](https://ollama.com/download), then download the model:

```bash
ollama pull llama3
```

Make sure Ollama is running before you choose **Ollama** in the app.

### 6. Run the app

```bash
python chipchap.py
```

---

## 💬 How to Use

1. Pick a backend, **OpenAI** or **Ollama**, from the dropdown at the top.
2. Type your message and press **Enter** or click **➤**.
3. ChipChap shows a thinking animation and then replies in the same chat bubble.
4. You can switch backends at any time. The conversation history is kept.

---

## 📁 Project Structure

```
chipchap/
├── chipchap.py        # Main application (GUI + AI logic)
├── requirements.txt   # Python dependencies
├── .env.example       # Template for your API key
├── .gitignore         # Keeps .env and the venv out of Git
└── README.md
```

---

## 🔮 Ideas for Future Improvements

- A **"New Chat"** button (the `new_chat()` function already exists and only needs to be connected in the UI)
- Light/dark theme toggle
- Saving and loading chat history
- Streaming responses word by word
- More selectable models (e.g. `phi3`, `mistral`)

---

## 👩‍💻 Author

**Iva Ivanova**: Software Development student 

---

> ⚠️ **Note:** Never commit your `.env` file. It contains your private API key. The included `.gitignore` already excludes it.
