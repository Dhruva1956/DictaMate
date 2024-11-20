from flask import Flask, request, render_template
from gtts import gTTS
from pydub import AudioSegment
import os

app = Flask(__name__)

# Ensure the static directory exists
STATIC_DIR = "static"
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("sentence", "")
        pause_time = float(request.form.get("pause_time", 1.0))  # Default to 1 second

        if sentence:
            try:
                words = sentence.split()
                combined_audio = AudioSegment.silent(duration=0)  # Start with silence

                for word in words:
                    # Generate speech for each word
                    tts = gTTS(text=word, lang="en")
                    word_audio_file = os.path.join(STATIC_DIR, f"{word}.mp3")
                    tts.save(word_audio_file)

                    # Load the audio file into pydub
                    word_audio = AudioSegment.from_mp3(word_audio_file)

                    # Add the word audio to the combined audio
                    combined_audio += word_audio

                    # Add a pause after each word (in milliseconds)
                    combined_audio += AudioSegment.silent(duration=pause_time * 1000)

                # Save the final combined audio
                output_file = os.path.join(STATIC_DIR, "output.mp3")
                combined_audio.export(output_file, format="mp3")

                # Clean up temporary word files
                for word in words:
                    temp_file = os.path.join(STATIC_DIR, f"{word}.mp3")
                    if os.path.exists(temp_file):
                        os.remove(temp_file)

                return render_template(
                    "index.html", message="Dictation complete!", audio_file="output.mp3"
                )
            except Exception as e:
                return render_template(
                    "index.html", error=f"An error occurred: {str(e)}"
                )
        else:
            return render_template("index.html", error="Please enter a sentence for dictation.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
