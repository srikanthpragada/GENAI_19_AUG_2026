import tkinter as tk
from tkinter import scrolledtext
from langchain.chat_models import init_chat_model

# Initialize Gemini through LangChain
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)


def ask_gemini():
    prompt = prompt_box.get("1.0", tk.END).strip()

    if not prompt:
        return

    response_box.config(state="normal")
    response_box.delete("1.0", tk.END)
    response_box.insert(tk.END, "Thinking...")
    response_box.config(state="disabled")

    try:
        response = model.invoke(prompt)

        response_box.config(state="normal")
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, response.content)
        response_box.config(state="disabled")

    except Exception as e:
        response_box.config(state="normal")
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, str(e))
        response_box.config(state="disabled")


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Gemini 2.5 Flash")
root.geometry("900x650")
root.configure(bg="#111111")

# Header
header = tk.Label(
    root,
    text="Gemini 2.5 Flash",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#111111"
)
header.pack(anchor="w", padx=25, pady=(20, 5))

subtitle = tk.Label(
    root,
    text="Ask anything",
    font=("Segoe UI", 10),
    fg="#999999",
    bg="#111111"
)
subtitle.pack(anchor="w", padx=27, pady=(0, 15))


# Prompt label
prompt_label = tk.Label(
    root,
    text="PROMPT",
    font=("Segoe UI", 9, "bold"),
    fg="#aaaaaa",
    bg="#111111"
)
prompt_label.pack(anchor="w", padx=25)


# Prompt box
prompt_box = scrolledtext.ScrolledText(
    root,
    height=7,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    relief="flat",
    padx=12,
    pady=12
)
prompt_box.pack(fill="x", padx=25, pady=(5, 12))


# Ask button
ask_button = tk.Button(
    root,
    text="ASK GEMINI",
    command=ask_gemini,
    font=("Segoe UI", 10, "bold"),
    bg="#eeeeee",
    fg="#111111",
    activebackground="#cccccc",
    activeforeground="#111111",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)
ask_button.pack(anchor="e", padx=25, pady=(0, 20))


# Response label
response_label = tk.Label(
    root,
    text="RESPONSE",
    font=("Segoe UI", 9, "bold"),
    fg="#aaaaaa",
    bg="#111111"
)
response_label.pack(anchor="w", padx=25)


# Response box
response_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="#eeeeee",
    insertbackground="white",
    relief="flat",
    padx=12,
    pady=12
)
response_box.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=(5, 25)
)

response_box.config(state="disabled")


root.mainloop()
