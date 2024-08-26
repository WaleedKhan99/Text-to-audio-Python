import gtts
import playsound

# Prompt the user for input text
text = input("Enter the text: ")

# Create a gTTS object with the specified language
language = "en-us"  # English (USA)
sound = gtts.gTTS(text, lang=language)

# Save the generated audio to a file
sound.save("audio.mp3")

# Play the saved audio
playsound.playsound("audio.mp3")


