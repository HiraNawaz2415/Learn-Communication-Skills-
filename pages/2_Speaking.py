import os
from dotenv import load_dotenv

import streamlit as st
import streamlit.components.v1 as components
import requests
from difflib import SequenceMatcher

# -----------------------------
# ✅ Load environment variables from .env
# -----------------------------
load_dotenv()

# ✅ Hugging Face API key from .env
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Whisper model endpoint
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"

st.set_page_config(page_title="🎙️ Speaking Practice with WAV Recorder")
st.title("🎙️ Speaking Practice — Record and Check")

# --------------------------------
# ✅ Dynamic Target Sentence Input
# --------------------------------
target_sentence = st.text_input(
    "Enter the sentence you want to practice 👇",
    "Good communication skills open doors to countless opportunities."
)

st.write("""
### 1️⃣ Record your sentence  
Click **Start Recording**, speak the sentence, then **Stop** and **Download** the WAV file.
""")

st.info(f"📢 **Target sentence:** _\"{target_sentence}\"_")

# ------------------------------
# 📼 WAV recorder (Recorder.js)
# ------------------------------
html_code = """
<!DOCTYPE html>
<html>
  <body>
    <h4>🎤 WAV Recorder</h4>
    <button id="recordButton">Start Recording</button>
    <button id="stopButton" disabled>Stop Recording</button>
    <p><a id="downloadLink"></a></p>

    <script>
      let gumStream;
      let rec;
      let input;
      let audioContext = new (window.AudioContext || window.webkitAudioContext)();

      const recordButton = document.getElementById("recordButton");
      const stopButton = document.getElementById("stopButton");
      const downloadLink = document.getElementById("downloadLink");

      recordButton.onclick = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        gumStream = stream;
        input = audioContext.createMediaStreamSource(stream);
        rec = new Recorder(input, { numChannels: 1 });
        rec.record();
        recordButton.disabled = true;
        stopButton.disabled = false;
      };

      stopButton.onclick = () => {
        rec.stop();
        gumStream.getAudioTracks()[0].stop();
        rec.exportWAV(blob => {
          const url = URL.createObjectURL(blob);
          downloadLink.href = url;
          downloadLink.download = "recording.wav";
          downloadLink.innerHTML = "⬇️ Download your WAV file";
        });
        recordButton.disabled = false;
        stopButton.disabled = true;
      };
    </script>

    <!-- Recorder.js library -->
    <script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
  </body>
</html>
"""

components.html(html_code, height=300)

# ------------------------------
# 2️⃣ Upload & transcribe
# ------------------------------
st.write("### 2️⃣ Upload your recorded file and check pronunciation")

uploaded_file = st.file_uploader(
    "📂 Upload your **recording.wav** file here",
    type=["wav"]
)

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    st.success("✅ File uploaded! Sending to Whisper...")

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": uploaded_file.type  # audio/wav
    }

    audio_data = uploaded_file.read()

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            data=audio_data,
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            transcript = result.get("text", "").strip()

            if transcript:
                st.subheader("📝 **Your Transcript:**")
                st.success(transcript)

                ratio = SequenceMatcher(None, transcript.lower(), target_sentence.lower()).ratio()
                match_percent = round(ratio * 100, 2)

                st.write(f"✅ **Match score:** {match_percent}%")

                if match_percent >= 80:
                    st.balloons()
                    st.success("🎉 Excellent! Your pronunciation is clear and accurate.")
                else:
                    st.warning("📢 Not bad — try again for better clarity.")
            else:
                st.error("❌ No text found in the audio. Try recording again.")

        else:
            st.error(f"❌ API Error: {response.status_code} — {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")

# ------------------------------
# 📚 Phonetics section
# ------------------------------
st.header("🔤 How to Pronounce English Sounds")
st.write("Learn the 44 phonemes of English with these videos.")
st.header("📚 English Phonemes — 44 Sounds")

st.markdown("""
**Vowels:**  
- Short Vowels: /ɪ/ /ʊ/ /e/ /ə/ /ʌ/ /æ/ /ɒ/  
- Long Vowels: /i:/ /u:/ /ɜ:/ /ɔ:/ /ɑ:/  
- Diphthongs: /eɪ/ /aɪ/ /ɔɪ/ /əʊ/ /aʊ/ /ɪə/ /eə/ /ʊə/

**Consonants:**  
- Plosives: /p/ /b/ /t/ /d/ /k/ /g/  
- Fricatives: /f/ /v/ /θ/ /ð/ /s/ /z/ /ʃ/ /ʒ/ /h/  
- Affricates: /tʃ/ /dʒ/  
- Nasals: /m/ /n/ /ŋ/  
- Approximants: /w/ /r/ /j/ /l/
""")

st.header("📽️ Learn Phonetic Sounds")
st.write("""
🎓 Click below to open each pronunciation lesson on YouTube in a new tab.
These videos are from trusted channels like BBC Learning English.
""")

st.subheader("🗣️ Short Vowels")
st.video("https://www.youtube.com/watch?v=DIWkl9HcGy4")

st.subheader("🗣️ Long Vowels")
st.video("https://www.youtube.com/watch?v=RmxByBumXxg")

st.subheader("🎵 Sing-along: Short Vowel Song")
st.video("https://www.youtube.com/watch?v=RUSCz41aDug")

st.subheader("🗣️ Short Vowels")
short_vowels = [
    {"symbol": "/ɪ/", "example": "sit", "audio": "CS/sounds/sit.mp3"},
    {"symbol": "/e/", "example": "bed", "audio": "CS/sounds/bed.mp3"},
    {"symbol": "/æ/", "example": "cat", "audio": "CS/sounds/cat.mp3"},
    {"symbol": "/ʌ/", "example": "cup", "audio": "CS/sounds/cup.mp3"},
    {"symbol": "/ɒ/", "example": "hot", "audio": "CS/sounds/hot.mp3"},
    {"symbol": "/ʊ/", "example": "put", "audio": "CS/sounds/put.mp3"},
    {"symbol": "/ə/", "example": "about", "audio": "CS/sounds/about.mp3"}
]
for s in short_vowels:
    st.markdown(f"**{s['symbol']}** — *{s['example']}*")
    st.audio(s["audio"])

st.subheader("🗣️ Long Vowels")
long_vowels = [
    {"symbol": "/iː/", "example": "see", "audio": "CS/sounds/see.mp3"},
    {"symbol": "/ɑː/", "example": "car", "audio": "CS/sounds/car.mp3"},
    {"symbol": "/ɔː/", "example": "saw", "audio": "CS/sounds/saw.mp3"},
    {"symbol": "/ɜː/", "example": "bird", "audio": "CS/sounds/bird.mp3"},
    {"symbol": "/uː/", "example": "blue", "audio": "CS/sounds/blue.mp3"}
]
for s in long_vowels:
    st.markdown(f"**{s['symbol']}** — *{s['example']}*")
    st.audio(s["audio"])

st.subheader("🗣️ Diphthongs")
diphthongs = [
    {"symbol": "/eɪ/", "example": "day", "audio": "CS/sounds/day.mp3"},
    {"symbol": "/aɪ/", "example": "my", "audio": "CS/sounds/my.mp3"},
    {"symbol": "/ɔɪ/", "example": "boy", "audio": "CS/sounds/boy.mp3"},
    {"symbol": "/aʊ/", "example": "now", "audio": "CS/sounds/now.mp3"},
    {"symbol": "/əʊ/", "example": "go", "audio": "CS/sounds/go.mp3"},
    {"symbol": "/ɪə/", "example": "here", "audio": "CS/sounds/here.mp3"},
    {"symbol": "/eə/", "example": "air", "audio": "CS/sounds/air.mp3"},
    {"symbol": "/ʊə/", "example": "tour", "audio": "CS/sounds/tour.mp3"}
]
for s in diphthongs:
    st.markdown(f"**{s['symbol']}** — *{s['example']}*")
    st.audio(s["audio"])

st.subheader("🗣️ Consonants")
consonants = [
    {"symbol": "/p/", "example": "pen", "audio": "CS/sounds/pen.mp3"},
    {"symbol": "/b/", "example": "back", "audio": "CS/sounds/back.mp3"},
    {"symbol": "/t/", "example": "tea", "audio": "CS/sounds/tea.mp3"},
    {"symbol": "/d/", "example": "dog", "audio": "CS/sounds/dog.mp3"},
    {"symbol": "/k/", "example": "cat", "audio": "CS/sounds/cat.mp3"},
    {"symbol": "/g/", "example": "go", "audio": "CS/sounds/go.mp3"},
    {"symbol": "/f/", "example": "fish", "audio": "CS/sounds/fish.mp3"},
    {"symbol": "/v/", "example": "van", "audio": "CS/sounds/van.mp3"},
    {"symbol": "/θ/", "example": "think", "audio": "CS/sounds/think.mp3"},
    {"symbol": "/ð/", "example": "this", "audio": "CS/sounds/this.mp3"},
    {"symbol": "/s/", "example": "see", "audio": "CS/sounds/see.mp3"},
    {"symbol": "/z/", "example": "zoo", "audio": "CS/sounds/zoo.mp3"},
    {"symbol": "/ʃ/", "example": "she", "audio": "CS/sounds/she.mp3"},
    {"symbol": "/ʒ/", "example": "vision", "audio": "CS/sounds/vision.mp3"},
    {"symbol": "/h/", "example": "house", "audio": "CS/sounds/house.mp3"},
    {"symbol": "/m/", "example": "man", "audio": "CS/sounds/man.mp3"},
    {"symbol": "/n/", "example": "no", "audio": "CS/sounds/no.mp3"},
    {"symbol": "/ŋ/", "example": "sing", "audio": "CS/sounds/sing.mp3"},
    {"symbol": "/l/", "example": "leg", "audio": "CS/sounds/leg.mp3"},
    {"symbol": "/r/", "example": "red", "audio": "CS/sounds/red.mp3"},
    {"symbol": "/j/", "example": "yes", "audio": "CS/sounds/yes.mp3"},
    {"symbol": "/w/", "example": "we", "audio": "CS/sounds/we.mp3"}
]
for s in consonants:
    st.markdown(f"**{s['symbol']}** — *{s['example']}*")
    st.audio(s["audio"])

st.success("🎉 Practice every sound — click, listen and repeat to improve your pronunciation!")
st.subheader("🎥 IPA Chart — Full Guide")
st.video("https://www.youtube.com/watch?v=1kAPHyHd7Lo")
