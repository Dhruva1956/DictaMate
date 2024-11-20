from flask import Flask, request, render_template
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("sentence", "")
        pause_time = float(request.form.get("pause_time", 1.0))  # Default to 1 second

        if sentence:
            try:
                # Generate speech using gTTS
                tts = gTTS(text=sentence, lang='en')
                audio_file = "static/output.mp3"
                tts.save(audio_file)

                # Optionally, you can play the file using a player
                os.system(f"mpg123 {audio_file}")

                return render_template(
                    "index.html", message="Dictation complete!", audio_file=audio_file
                )
            except Exception as e:
                return render_template(
                    "index.html", error=f"An error occurred: {str(e)}"
                )
        else:
            return render_template("index.html", error="Please enter a sentence for dictation.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
