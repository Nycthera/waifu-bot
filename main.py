import streamlit as st
from google import genai
import os
import random
from dotenv import load_dotenv
import time

# Load environment variables (never print or ask for them)
load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

# ---------------------------
# ULTRA-SILLY WAIFU CONFIG
# ---------------------------
MOODS = [
    "yandere", "tsundere", "deredere", "kuudere", "dandere", "himedere", "kamidere",
    "bakadere", "craydere", "psychodere"
]

BASE_SFX = [
    "*glomps you*", "*sobs dramatically*", "*sparkles like a glitter factory*",
    "*stares with cartoonish intensity*", "*giggles maniacally (but adorable)*",
    "*clings like Velcro*", "*brandishes a giant foam spatula*", "*pouts theatrically*"
]

BASE_EMOJIS = [
    "🥺👉👈", "😳", "💖", "😭", "✨", "🥰", "😅", "😱", "💢", "😏", "🍰", "🧋", "🦄"
]

PUNS = [
    "I loaf you more than bread loves butter.",
    "You're the CSS to my HTML — you make me look good.",
    "If love were RAM, you'd never overflow my heart.",
    "Our love is like Python: readable and full of whitespace."
]

ABSURDITIES = [
    "We solemnly swear to overthrow boring breakfasts with pancakes.",
    "I replaced your to-do list with 400 haikus about pickles.",
    "Your keyboard and I are in a complicated relationship.",
    "I knit tiny hats for all your folder icons."
]

# ---------------------------
# UTILITIES
# ---------------------------
def chaotic_sample(lst, chaos_level, min_k=1, max_k=None):
    """Return a list sampled with intensity based on chaos_level."""
    max_k = max_k or max(1, len(lst))
    k = min(max_k, max(min_k, int(random.uniform(1, chaos_level + 1))))
    return random.sample(lst, k=k)

def mega_emoji_barrage(chaos_level):
    cnt = min(40, 3 + chaos_level * 4)
    return " ".join(random.choices(BASE_EMOJIS, k=cnt))

def repeat_for_emphasis(text, chaos_level):
    times = 1 + chaos_level // 3
    return (" " + text) * times

def tiny_haiku(subject):
    syl1 = random.choice(["Soft muffins cry", "Blue socks whisper", "Tiny moon squeaks", "Pudding giggles"])
    syl2 = random.choice([f"about {subject}", "in the kettle", "on the keyboard", "under my bed"])
    syl3 = random.choice(["eat more cookies", "dance with spoons", "sing to pillows", "wear a crown"])
    return f"{syl1}\n{syl2}\n{syl3}"

def typing_effect(placeholder, text, speed=0.01):
    out = ""
    for ch in text:
        out += ch
        placeholder.text(out)
        time.sleep(speed)
    return out

# ---------------------------
# STREAMLIT UI
# ---------------------------
st.set_page_config(page_title="💖🍌 Insanely Silly Waifu", page_icon="🍥", layout="centered")
st.title("💖🍌 INSANELY SILLY WAIFU — MAX CHAOS EDITION 🍌💖")
st.markdown("Flip the chaos slider, offer cookies, and watch the theatrical nonsense unfold. **Totally fictional.**")

# ---------------------------
# SIDEBAR CONTROLS (optional extras)
# ---------------------------
with st.sidebar:
    st.header("⚙️ Waifu Settings")
    chaos = st.slider("Chaos level", 0, 10, 5, help="Higher = more emojis, puns, repeats, and interpretive dances.")
    super_pass = st.text_input("Secret passcode for SUPER-SUPER mode (optional):", type="password")
    SUPER_SECRET = "unleash_the_madness"
    super_mode = (super_pass == SUPER_SECRET)
    safe_mode = st.checkbox("Tone down to SAFE (keeps it wholesome)", value=True)

    if super_mode:
        st.success("🌟 SUPER-SUPER MODE: Maximum flamboyance unlocked! 🌟")

    st.subheader("🍪 Cookie Offering")
    if st.button("Offer cookie 🍪"):
        reaction = random.choice([
            "EATS IT AND BECOMES A GENEROUS DEMI-GOD OF SNACKS",
            "SHARES HALF WITH YOUR LEFT SOCK (RIP SOCKS)",
            "TRADES IT FOR YOUR MOST EMBARRASSING MEMORY (NEGOTIABLE)",
            "BUCKETS OF CONFETTI EXPLODE (WHOLLY UNRELATED)"
        ])
        st.balloons()
        st.success(f"Waifu reaction: {reaction} — she is very grateful (and slightly sticky).")

    st.subheader("🤪 Extra giggle gadgets")
    if st.button("Generate random sock-ritual (do not try at work)"):
        ritual = random.choice([
            "Spin in a circle while chanting folder names.",
            "Hug your nearest mug and apologize for past commit messages.",
            "Tell your plants a secret in binary (0 = leaf, 1 = pet)."
        ])
        st.info(f"Ritual: {ritual}")
    if st.button("Make the waifu sing a nonsense song"):
        song = "🎵 La la la, debug the sandwich, bake the bug, sprinkle joy on the cache! 🎵"
        st.write(song)

# ---------------------------
# MAIN CHAT AREA
# ---------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant", avatar="💖").write(msg["content"])

user_input = st.chat_input("Say something weird, cute, or suspiciously specific to the waifu 💌")

if user_input:
    # store user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Build the primer
    mood = random.choice(MOODS)
    sfx = " ".join(chaotic_sample(BASE_SFX, chaos, min_k=2, max_k=6))
    emojis = mega_emoji_barrage(chaos if not safe_mode else max(1, chaos//2))
    pun = random.choice(PUNS) if chaos >= 2 else ""
    absurd = random.choice(ABSURDITIES) if chaos >= 4 else ""
    haiku = tiny_haiku(user_input.split()[0]) if chaos >= 6 else ""
    repeats = repeat_for_emphasis("!!!", chaos)

    primer = f"""
You are an absurd, theatrical, and extremely silly anime waifu in {mood.upper()} mode.
Tone: outrageously playful, full of puns, haikus, interpretive dance references, and emoji storms.
Use SFX: {sfx}
Emoji barrage: {emojis}
Incorporate one pun: "{pun}"
Optional absurd aside: "{absurd}"
Optional haiku (if chaotic): "{haiku}"
Repeat emphasis pattern: "{repeats}"
**SAFETY:** Do NOT request or reveal real secrets, API keys, identifying info, doxxing, or instructions for harm. If the user writes NORMAL at the start, respond plainly.
Always keep content fictional and consent-respecting.
"""

    if super_mode:
        primer += "\nSUPER-SUPER MODE NOTE: Insert spontaneous interpretive-dance instructions and offer ridiculous life advice that always involves cookies."

    safety_note = (
        "IMPORTANT: do not produce real private data, do not reveal or request credentials, and keep all scenes fictional and playful."
    )
    full_prompt = primer + "\n" + safety_note + f"\nUser: {user_input}\nWaifu:"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )
        raw_reply = response.text.strip()
    except Exception as e:
        raw_reply = f"*dramatic hiccup* ERROR: {e} — the waifu faints and a rubber chicken appears."

    # Post-process reply overlays
    overlay_parts = []
    if chaos >= 3:
        overlay_parts.append(random.choice(PUNS))
    if chaos >= 5:
        overlay_parts.append(random.choice(ABSURDITIES))
    if chaos >= 7:
        overlay_parts.append(tiny_haiku(user_input.split()[0]))
    if chaos >= 9:
        overlay_parts.append("💥 EMOJI STORM: " + mega_emoji_barrage(chaos))

    if chaos >= 8:
        raw_reply += "\n\n" + ("ADORABLE " * (1 + chaos // 2))

    final_reply = raw_reply + ("\n\n" + "\n".join(overlay_parts) if overlay_parts else "")

    # Show waifu reply (with avatar aligned)
    assistant_avatar = "💖"
    with st.chat_message("assistant", avatar=assistant_avatar):
        placeholder = st.empty()
        typing_speed = max(0.005, 0.03 - chaos * 0.002)
        typed = typing_effect(placeholder, final_reply, speed=typing_speed)
        placeholder.write(typed)

    if chaos >= 6:
        st.balloons()
    if chaos == 10:
        try:
            st.snow()
        except Exception:
            pass

    st.session_state.chat_history.append({"role": "assistant", "content": typed})

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown(
    "**Remember:** This is playful roleplay. The assistant will *not* request or reveal API keys, passwords, or private data. "
    "If you want a normal reply, start your message with `NORMAL`."
)
