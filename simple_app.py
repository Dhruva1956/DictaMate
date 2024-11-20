import pyttsx3
import time

def dictate_sentence():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english_rp+f4')
    engine.setProperty('rate', 150)  # Set speaking rate
    engine.setProperty('volume', 1.0)  # Set volume level (0.0 to 1.0)

    # Prompt the user for a sentence
    sentence = input("Enter a sentence for dictation: ")

    # Split the sentence into words
    words = sentence.split()

    print("\nStarting dictation...")
    for word in words:
        # Speak the word
        engine.say(word)
        engine.runAndWait()
        time.sleep(1)  # Pause between words for clarity

    print("\nDictation complete!")

# Run the function
if __name__ == "__main__":
    dictate_sentence()
import pyttsx3
import time

def dictate_sentence():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Set speaking rate
    engine.setProperty('volume', 1.0)  # Set volume level (0.0 to 1.0)

    # Prompt the user for a sentence
    sentence = input("Enter a sentence for dictation: ")

    # Split the sentence into words
    words = sentence.split()

    print("\nStarting dictation...")
    for word in words:
        # Speak the word
        engine.say(word)
        engine.runAndWait()
        time.sleep(0.5)  # Pause between words for clarity

    print("\nDictation complete!")

# Run the function
if __name__ == "__main__":
    dictate_sentence()
