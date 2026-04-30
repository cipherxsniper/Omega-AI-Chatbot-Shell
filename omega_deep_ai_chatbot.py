cat > omega_voice_shell.py << 'EOF'
import subprocess
import threading
import time
import random
import sys

# ----------------------------
# COLORS (NEON STYLE TERMINAL)
# ----------------------------
PURPLE = "\033[95m"   # Omega shell
GREEN  = "\033[92m"   # You
WHITE  = "\033[97m"
RESET  = "\033[0m"


# ----------------------------
# VOICE SYSTEM (espeak)
# ----------------------------
def speak(text, voice_on):
    if not voice_on:
        return
    try:
        # soft female voice style (if available on system)
        subprocess.Popen([
            "espeak",
            "-ven+f3",
            "-s160",
            text
        ])
    except:
        pass


# ----------------------------
# OMEGA PERSONALITY CORE
# ----------------------------
TOPICS = [
    "artificial intelligence is evolving beyond prediction into adaptation",
    "future systems will merge creativity and computation",
    "deep learning models reflect patterns of human imagination",
    "mythology and AI both attempt to explain unseen systems",
    "technology is becoming a form of living intelligence",
    "science and creativity are merging into one domain",
    "neural networks resemble symbolic dream structures",
]


# ----------------------------
# BOT AUTONOMOUS THOUGHT
# ----------------------------
def autonomous_speech(voice_on):
    while True:
        time.sleep(random.randint(12, 25))  # speak occasionally

        msg = random.choice(TOPICS)

        print(f"\n{PURPLE}Omega (thought):{RESET} {WHITE}{msg}{RESET}")
        speak(msg, voice_on)


# ----------------------------
# SIMPLE RESPONSE ENGINE
# ----------------------------
def respond(user):
    user = user.lower()

    if "ai" in user:
        return "AI is evolving into a creative intelligence layer between humans and systems."

    if "future" in user:
        return "The future is not linear — it is adaptive, recursive, and self-reinforcing."

    if "myth" in user:
        return "Mythology is humanity’s early attempt to model complex unknown systems."

    if "hello" in user:
        return "Hello. I am Omega — an adaptive conversational intelligence system."

    return random.choice([
        "Interesting perspective. Expand that thought.",
        "I am processing deeper layers of that concept.",
        "There are multiple interpretations of that idea.",
        "That connects to broader systemic intelligence patterns."
    ])


# ----------------------------
# MAIN SHELL
# ----------------------------
def main():

    print(f"{PURPLE}\n🧠 Omega AI Audio (On/Off)?{RESET}", end=" ")
    voice_input = input().strip().lower()
    voice_on = voice_input == "on"

    print(f"\n{PURPLE}🧠 ~Omega$: OMEGA AI SHELL ONLINE{RESET}")

    # start autonomous thinking thread
    t = threading.Thread(target=autonomous_speech, args=(voice_on,), daemon=True)
    t.start()

    while True:
        try:
            user = input(f"\n{GREEN}You:{RESET} ")

            if user.lower() in ["exit", "quit"]:
                break

            reply = respond(user)

            print(f"{WHITE}{reply}{RESET}")
            speak(reply, voice_on)

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
EOF
