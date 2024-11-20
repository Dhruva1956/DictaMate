from flask import Flask, request, render_template
import pyttsx3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("sentence", "")
        pause_time = float(request.form.get("pause_time", 1.0))  # Default to 1 second

        if sentence:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Set speaking rate
            engine.setProperty('volume', 1.0)  # Set volume level

            # Set voice explicitly if needed
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # Use a valid voice index

            for word in sentence.split():
                engine.say(word)
                engine.runAndWait()

            return render_template("index.html", message="Dictation complete!")
        else:
            return render_template("index.html", error="Please enter a sentence for dictation.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(app, host='0.0.0.0', debug=True, port=5000)
    #app.run(debug=True)
