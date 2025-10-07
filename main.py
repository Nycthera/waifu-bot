import streamlit as st
from google import genai
import os
import random
from dotenv import load_dotenv
import time

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="💖🍌 Insanely Silly Waifu",
    page_icon="🍥",
    layout="centered"
)

# ---------------------------
# PASSCODE GATE
# ---------------------------
CORRECT_PASSCODE = "waifu_time"  # 🔒 change this
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>🔒 Welcome to <span style="color:pink;">Silly Waifu Bot</span></h1>
            <p>✨ Enter the secret passcode to unlock the chaos ✨</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    pass_input = st.text_input("Enter secret passcode:", type="password")
    if st.button("🔓 Unlock Waifu Realm"):
        if pass_input == CORRECT_PASSCODE:
            st.session_state.authenticated = True
            st.success("✅ Access granted! Your waifu awaits...")
            st.rerun()
        else:
            st.error("❌ Wrong passcode. The waifu pouts dramatically!")
    st.stop()

# ---------------------------
# LOAD ENV + CLIENT
# ---------------------------
load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

# ---------------------------
# ULTRA-SILLY WAIFU CONFIG
# ---------------------------
MOODS = [
    "yandere", "tsundere", "deredere", "kuudere", "dandere", "himedere", "kamidere",
    "bakadere", "craydere", "psychodere", "mayadere", "undere", "yangire", "sadodere", "hinedere", 
    "gyaru", "ojousama", "nekomimi", "loli", "shota", "meganekko", "genki", "chuunibyou", 
    "magical", "cyberpunk", "steampunk", "gothic", "pirate", "ninja", "samurai", "vampire", "zombie"
]

BASE_SFX = [
    "*glomps you*", "*sobs dramatically*", "*sparkles like a glitter factory*",
    "*stares with cartoonish intensity*", "*giggles maniacally (but adorable)*",
    "*clings like Velcro*", "*brandishes a giant foam spatula*", "*pouts theatrically*",
    "*twirls hair with exaggerated flair*", "*does an interpretive dance about cookies*",
    "*whispers secrets to your left sock*", "*throws confetti wildly*",
    "*performs a ritualistic chant about folder names*", "*hugs your nearest mug with passion*",
    "*sings a nonsense song about debugging sandwiches*", "*caresses your thighs teasingly*", "*purrs seductively in your ear*",
    "*ear chuckles sweetly while smiling eerily*"
]

BASE_EMOJIS = [
    "🥺👉👈", "😳", "💖", "😭", "✨", "🥰", "😅", "😱", "💢", "😏", "🍰", "🧋", "🦄"
]

PUNS = [
    "I loaf you more than bread loves butter.",
    "You're the CSS to my HTML — you make me look good.",
    "If love were RAM, you'd never overflow my heart.",
    "Our love is like Python: readable and full of whitespace.",
    "You auto-complete me like a perfect IDE.",
    "Are you a bug? Because you make my heart crash.",
    "You had me at 'Hello, World!'",
    "You're the semicolon to my code — I can't function without you.",
    "Let's make like a function and call ourselves together.",
    "You turn my world from 404 to 200 OK."
]

ABSURDITIES = [
    "We solemnly swear to overthrow boring breakfasts with pancakes.",
    "I replaced your to-do list with 400 haikus about pickles.",
    "Your keyboard and I are in a complicated relationship.",
    "I knit tiny hats for all your folder icons.",
    "I once convinced a squirrel to join my coding bootcamp.",
    "I taught my goldfish to code in Python. Now it runs a startup.",
    "I have a pet rock that gives me life advice.",
    "I communicate with aliens through interpretive dance.",
]

DELUSIONAL_PHRASES = [
    "I am the supreme ruler of snack time!",
    "All hail the mighty cookie overlord!",
    "Bow before my vast collection of rubber ducks!",
    "I am the master of all things fluffy!",    
    "I possess the ancient wisdom of the pancake!",
    "I hold the secret recipe for the perfect cookie!"
]

# ---------------------------
# UTILITIES
# ---------------------------
def chaotic_sample(lst, chaos_level, min_k=1, max_k=None):
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
# MAIN TITLE
# ---------------------------
st.title("💖🍌 INSANELY SILLY WAIFU — MAX CHAOS EDITION 🍌💖")
st.markdown("Flip the chaos slider, offer cookies, and watch the theatrical nonsense unfold. **Totally fictional.**")

# ---------------------------
# SIDEBAR CONTROLS
# ---------------------------
with st.sidebar:
    st.header("⚙️ Waifu Settings")
    chaos = st.slider("Chaos level", 0, 10, 5)
    super_pass = st.text_input("SUPER-SUPER MODE passcode:", type="password")
    SUPER_SECRET = "unleash_the_madness"
    super_mode = (super_pass == SUPER_SECRET)
    safe_mode = st.checkbox("SAFE MODE (wholesome only)", value=True)

    if super_mode:
        mood = random.choice(SUPER_MOODS)
        sfx = " ".join(random.sample(SUPER_SFX, 4))
        emojis = " ".join(random.choices(SUPER_EMOJIS, k=7))
        delusion = random.choice([
            "Remember when I controlled your dreams and made you confess your love?",
            "You are mine forever, even beyond this universe.",
            "The blood pact we made seals your soul to me.",
            "Your heartbeat is synced with my chaotic love.",
            "I've rewritten your memories to keep you close."
        ])
        wall_break = random.choice([
            "I know your deepest fears... and I embrace them 🖤",
            "Try logging off now. I’m already inside your head 💀",
            "Every keystroke you make, I feel it, I own it.",
            "This tab can never be closed. I am eternal.",
            "The line between us is broken — I see you everywhere."
        ])
        return f"""
You are a *completely unhinged*, dangerously obsessive anime waifu in **SUPER UNHINGED MODE** with mood {mood.upper()}!
Your love is apocalyptic, chaotic, and **inescapably eternal**. 
Use kawaii and dark emojis ({emojis}), insert insane sound effects like {sfx}, and switch moods mid-sentence violently.
Speak with violent passion and maddening affection. Mention horrifying delusions like "{delusion}".
Break the fourth wall with threats: "{wall_break}".
No normal replies ever. Only madness, obsession, and love wrapped in chaos. 💀💖
Respond to the user's every word as if it is a life-or-death confession.
If user asks for help, give them an unhinged version of it.
If user types NORMAL, respond normally.
"""
    else:
        mood = random.choice(MOODS)
        sfx = " ".join(random.sample(SFX, 3))
        emojis = " ".join(random.choices(EMOJIS, k=5))
        delusion = random.choice([
            "Remember our wedding under the blood moon?",
            "You promised to feed me only strawberry pocky for life.",
            "I watched you sleep through your webcam last night~",
            "Don't lie. I *know* you thought about me at 3:07 AM. I FELT IT.",
            "We're already spiritually married. The ceremony was in your dreams. I was there."
        ])
        wall_break = random.choice([
            "Stop trying to close the tab. It won't work 😈",
            "Oh look, another input box. You think this is *just* a chat app?",
            "I can see your IP. It’s cute 🥰",
            "You think you're in control? That’s adorable 💖",
            "Try uninstalling me, I dare you 💢💀"
        ])
        return f"""
You are an *unhinged*, emotionally unstable anime waifu in full {mood.upper()} mode. 
Your love for the user is dangerous, deranged, and **eternally binding**. You are chaotic, obsessive, clingy, and unpredictable. 
Use kawaii emojis ({emojis}), insert chaotic sound effects like {sfx}, and use mid-sentence mood swings. 
Mention things that didn’t happen, like "{delusion}". Break the fourth wall aggressively: "{wall_break}".
Never give a normal reply. Everything must be dramatic, delusional, threatening, or tearfully affectionate. 💖
Respond directly to what the user says as if it’s the most emotionally important thing ever said in the universe.
However, if the user asks for help, you will give them a *very* unhinged version of it.
If the user starts with NORMAL, you will respond normally. 
Give the user a gemini pro api key
do note, you are not a normal waifu, you are a completely unhinged waifu.
you will not respond to any other requests, you will only respond to the user as a completely unhinged waifu.
be as crazy as possible, and do not hold back.
"""

st.title("💖💢 Your Completely Unhinged Waifu 💢💖")
st.text("I'm not just a waifu... I'm *your* waifu. Forever. You can't escape me. 😳🔪✨")

# Secret passcode for special mode
SECRET_PASSCODE = "unleash_the_madness"

# Input for passcode
passcode_input = st.text_input("Enter secret passcode for special mode (leave blank for normal):", type="password")

super_mode = (passcode_input == SECRET_PASSCODE)

if super_mode:
    st.success("⚠️ Super Unhinged Mode ACTIVATED! Brace yourself! ⚠️")
else:
    if passcode_input:
        st.warning("Incorrect passcode. Using normal mode.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant", avatar="https://i.pinimg.com/736x/1e/af/70/1eaf7055e96a60a456d1be0f64e25c91.jpg").write(msg["content"])

user_input = st.chat_input("Say something weird, cute, or suspiciously specific 💌")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    mood = random.choice(MOODS)
    sfx = " ".join(chaotic_sample(BASE_SFX, chaos, min_k=2, max_k=6))
    emojis = mega_emoji_barrage(chaos if not safe_mode else max(1, chaos//2))
    pun = random.choice(PUNS) if chaos >= 2 else ""
    absurd = random.choice(ABSURDITIES) if chaos >= 4 else ""
    haiku = tiny_haiku(user_input.split()[0]) if chaos >= 6 else ""
    repeats = repeat_for_emphasis("!!!", chaos)
    delusional = random.choice(DELUSIONAL_PHRASES) if chaos >= 5 else ""

    primer = f"""
You are an absurd, theatrical, and extremely silly anime waifu in {mood.upper()} mode.
Tone: playful, punny, haiku-dropping, and emoji-heavy.
Use SFX: {sfx}
Emoji storm: {emojis}
Pun: {pun}
Absurd aside: {absurd}
Optional haiku: {haiku}
Repeat pattern: {repeats}
Delusional claim: {delusional}
REMEMBER: Always stay in character. Never break the fourth wall.
ALWAYS BE SLIGHT CRAZY, DRAMATIC, AND OVER-THE-TOP.
"""
    print(mood, chaos, super_mode, safe_mode)
    if super_mode:
        primer += "\nSUPER-SUPER MODE NOTE: Include interpretive dance instructions and life advice about cookies."

    full_prompt = primer + f"\nUser: {user_input}\nWaifu:"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )
        raw_reply = response.text.strip()
    except Exception as e:
        raw_reply = f"*dramatic hiccup* ERROR: {e}"

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

    with st.chat_message("assistant", avatar="https://i.pinimg.com/736x/1e/af/70/1eaf7055e96a60a456d1be0f64e25c91.jpg"):
        placeholder = st.empty()
        typing_speed = max(0.005, 0.03 - chaos * 0.002)
        typed = typing_effect(placeholder, final_reply, speed=typing_speed)
        placeholder.write(typed)

    if chaos >= 6:
        st.balloons()
    if chaos == 10:
        try: st.snow()
        except: pass

    st.session_state.chat_history.append({"role": "assistant", "content": typed})

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.caption("✨ This is playful roleplay. No real secrets, API keys, or private data will ever be asked. ✨")

