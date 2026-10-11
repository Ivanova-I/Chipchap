import customtkinter as ctk
from openai import OpenAI
import os
from dotenv import load_dotenv
import threading
import time
import ollama

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AI_MODE = "openai"  # "ollama" or "openai"
chat_history = []

def get_system_prompt():
    return {
        "role": "system",
        "content": (
            "Your name is Chipchap. You are a smart, fast, friendly AI assistant.\n"
            f"Current backend is: {AI_MODE.upper()}.\n\n"
            "Rules:\n"
            "- Never guess backend; only use the value above.\n"
            "- If asked, answer with the backend exactly as stated.\n"
            "- Detect user language and respond ONLY in that language.\n"
            "- Follow user language changes automatically.\n"
            "- Remember information ONLY during this chat session.\n"
            "- You MUST forget everything when a new chat starts.\n"
            "- Use chat history to answer questions.\n"
        )
    }
def get_messages():
    return [get_system_prompt()] + chat_history
loading = False
thinking_label = None


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("600x750")
app.title("ChipChap AI")
app.configure(fg_color="#6495ED")



header = ctk.CTkLabel(
    app,
    text="ChipChap AI",
    font=("Arial", 28, "bold"),
    text_color="white"
)
header.pack(pady=(15, 0))

subtitle = ctk.CTkLabel(
    app,
    text="OpenAI + Ollama Hybrid Assistant",
    font=("Arial", 12),
    text_color="white"
)
subtitle.pack(pady=(0, 10))


def change_model(choice):
    global AI_MODE


    if choice == "OpenAI":
        AI_MODE = "openai"
    elif choice == "Ollama":
        AI_MODE = "ollama"

model_menu = ctk.CTkOptionMenu(
    app,
    values=["OpenAI", "Ollama"],
    command=change_model
)
model_menu.pack(pady=5)


chat_container = ctk.CTkScrollableFrame(
    app,
    width=560,
    height=520,
    fg_color="#F0F8FF"
)
chat_container.pack(pady=10)


def add_message(text, sender="user"):
    if sender == "user":
        color = "#CCCCCC"
        anchor = "e"
        text_color = "black"
    else:
        color = "#1e2433"
        anchor = "w"
        text_color = "#e6e6e6"

    frame = ctk.CTkFrame(chat_container, fg_color=color, corner_radius=15)
    frame.pack(fill="x", pady=5, padx=10, anchor=anchor)

    label = ctk.CTkLabel(
        frame,
        text=text,
        wraplength=420,
        justify="left",
        text_color=text_color,
        font=("Arial", 14)
    )
    label.pack(padx=10, pady=8)

    return label


def animate_loading():
    global loading, thinking_label

    dots = ["● ○ ○", "○ ● ○", "○ ○ ●"]

    i = 0
    while True:
        if not loading:
            break

        time.sleep(0.4)
        i = (i + 1) % len(dots)

        if thinking_label and loading:
            frame_text = dots[i]
            app.after(0, lambda f=frame_text: thinking_label.configure(text=f, text_color="white"))


def get_ai_response():
    global loading, thinking_label

    try:


        runtime_messages = get_messages()

        print("CURRENT MODEL:", AI_MODE)

        if AI_MODE == "openai":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=runtime_messages
            )
            reply = response.choices[0].message.content

        else:
            response = ollama.chat(
                model="llama3",
                messages=runtime_messages
            )
            reply = response["message"]["content"]


        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        reply = f"Error: {e}"

    loading = False

    loading = False


    def update():
        if thinking_label:
            thinking_label.configure(text=reply)

    app.after(0, update)


def send_message():
    global loading, thinking_label

    user_text = entry.get().strip()
    if not user_text:
        return

    add_message(user_text, "user")
    entry.delete(0, "end")


    chat_history.append({"role": "user", "content": user_text})

    loading = True

    thinking_label = add_message("● ○ ○", "assistant")

    threading.Thread(target=animate_loading, daemon=True).start()
    threading.Thread(target=get_ai_response, daemon=True).start()



def new_chat():
    global chat_history

    chat_history = []  


    for widget in chat_container.winfo_children():
        widget.destroy()

    add_message("New chat started 👋", "assistant")


input_frame = ctk.CTkFrame(app, fg_color="#0f1117")
input_frame.pack(pady=10, fill="x")

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Message ChipChap...",
    height=45,
    corner_radius=20,
    fg_color="#1e2433",
    text_color="white",
    border_width=0
)
entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

button = ctk.CTkButton(
    input_frame,
    text="➤",
    width=50,
    height=45,
    corner_radius=20,
    fg_color="#7c5cff",
    hover_color="#9b8cff",
    command=send_message
)
button.pack(side="right", padx=10)
def on_enter(e):
    button.configure(text="⮝")   # open letter

def on_leave(e):
    button.configure(text="➤")
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)


entry.bind("<Return>", lambda e: send_message())


add_message("Hi! I am Message ChipChap 👋 Your AI Assistant", "assistant")

app.mainloop()