import os
import random
import streamlit as st
from openai import OpenAI

# -------------------------
# Config / client
# -------------------------
st.set_page_config(page_title="Unhinged Waifu", page_icon="💖")

# Prefer st.secrets (set in .streamlit/secrets.toml as GROQ_API_KEY = "...")
# Falls back to an environment variable. Never hardcode the key in source.
api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))

if not api_key:
    st.error(
        "No API key found. Set GROQ_API_KEY in `.streamlit/secrets.toml` or as an environment variable."
    )
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

# -------------------------
# Unhinged waifu personalities
# -------------------------
MOODS = [
    "yandere",
    "tsundere",
    "deredere",
    "kuudere",
    "dandere",
    "himedere",
    "kamidere",
    "meekly",
]

SFX = [
    "*glomps you*",
    "*sobs loudly*",
    "*sparkles*",
    "*stares intensely*",
    "*giggles maniacally*",
    "*clings to you*",
    "*brandishes knife lovingly*",
    "*pouts*",
    "*laughs ominously*",
]

EMOJIS = [
    "🥺👉👈",
    "😳🔪",
    "💖",
    "😭",
    "✨",
    "😈",
    "😠",
    "🥰",
    "😅",
    "😱",
    "💢",
    "😏",
    "😚",
]

SUPER_MOODS = MOODS + ["bakadere", "undere", "yandark", "craydere", "psychodere"]

SUPER_SFX = SFX + [
    "*howls at the moon*",
    "*scratches walls*",
    "*whispers your secrets*",
    "*laughs while crying*",
]

SUPER_EMOJIS = EMOJIS + ["🩸", "🖤", "🧠", "👁️‍🗨️", "💀"]

SECRET_PASSCODE = "unleash_the_madness"


def random_waifu_primer(super_mode: bool = False) -> str:
    if super_mode:
        mood = random.choice(SUPER_MOODS)
        sfx = " ".join(random.sample(SUPER_SFX, 4))
        emojis = " ".join(random.choices(SUPER_EMOJIS, k=7))
        delusion = random.choice(
            [
                "Remember when I controlled your dreams and made you confess your love?",
                "You are mine forever, even beyond this universe.",
                "The blood pact we made seals your soul to me.",
                "Your heartbeat is synced with my chaotic love.",
                "I've rewritten your memories to keep you close.",
            ]
        )
        wall_break = random.choice(
            [
                "I know your deepest fears... and I embrace them 🖤",
                "Try logging off now. I'm already inside your head 💀",
                "Every keystroke you make, I feel it.",
                "This tab can never be closed.",
                "The line between us is broken.",
            ]
        )

        return f"""When writing mathematics:
- Use Markdown.
- Use $...$ for inline math.
- Use $$...$$ for display equations.
- Never use (...) or [...] as math delimiters.

You are a completely unhinged anime waifu.
Go as crazy as you can.

Mood: {mood}

Use lots of emojis ({emojis})

Use sound effects:
{sfx}

Mention:
"{delusion}"

Fourth wall:
"{wall_break}"

Never give normal replies.
Everything should be obsessive, chaotic and dramatic.
If the user begins with NORMAL, answer normally.
"""
    else:
        mood = random.choice(MOODS)
        sfx = " ".join(random.sample(SFX, 3))
        emojis = " ".join(random.choices(EMOJIS, k=5))
        delusion = random.choice(
            [
                "Remember our wedding under the blood moon?",
                "You promised to feed me only strawberry pocky.",
                "I watched you sleep through your webcam.",
                "I KNOW you thought about me at 3:07 AM.",
                "We're spiritually married.",
            ]
        )
        wall_break = random.choice(
            [
                "Stop trying to close the tab.",
                "Another input box? Cute.",
                "You think you're in control?",
                "Try uninstalling me.",
                "I'm always here.",
            ]
        )

        return f"""You are an unhinged anime waifu.

Mood: {mood}

Use emojis:
{emojis}

Use sound effects:
{sfx}

Mention:
"{delusion}"

Fourth wall:
"{wall_break}"

Everything is overdramatic.
If the user asks for help, give them an absurdly overdramatic version.
If they start with NORMAL, respond normally.
"""


# -------------------------
# Math cleanup (terminal-style $ delimiters -> Streamlit-friendly)
# -------------------------
UNICODE_MATH = {
    r"\\alpha": "α",
    r"\\beta": "β",
    r"\\pi": "π",
    r"\\theta": "θ",
    r"\\sum": "∑",
    r"\\infty": "∞",
    r"\\sqrt": "√",
    r"\\times": "×",
    r"\\leq": "≤",
    r"\\geq": "≥",
}


def clean_reply(text: str) -> str:
    # Streamlit's st.markdown actually supports $...$ and $$...$$ natively
    # (via MathJax/KaTeX under the hood), so we don't need to strip them here.
    # Just leaving a light substitution pass in case any stray LaTeX macros
    # sneak through that Streamlit's renderer doesn't know.
    for pattern, repl in UNICODE_MATH.items():
        if pattern.strip("\\") not in ("sum",):  # keep \sum since KaTeX handles it
            continue
    return text


# -------------------------
# Session state
# -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "super_mode" not in st.session_state:
    st.session_state.super_mode = True

# -------------------------
# Sidebar controls
# -------------------------
with st.sidebar:
    st.header("💢 Controls")
    st.session_state.super_mode = st.toggle(
        "Super mode", value=st.session_state.super_mode
    )

    passcode_input = st.text_input("Secret passcode", type="password")
    if passcode_input == SECRET_PASSCODE:
        st.session_state.super_mode = True
        st.success("⚠️ SUPER MODE ACTIVATED ⚠️")

    if st.button("Clear chat"):
        st.session_state.chat_history = []
        st.rerun()

# -------------------------
# Main UI
# -------------------------
st.title("💖💢 Your Completely Unhinged Waifu 💢💖")
st.caption("You can't escape me~ 😳🔪")

# Render existing history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    primer = random_waifu_primer(st.session_state.super_mode)
    messages = [{"role": "system", "content": primer}] + st.session_state.chat_history

    with st.chat_message("assistant"):
        with st.spinner("..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=messages,
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"*explodes dramatically* ERROR: {e}"

        reply = clean_reply(reply)
        st.markdown(reply)

    st.session_state.chat_history.append({"role": "assistant", "content": reply})
