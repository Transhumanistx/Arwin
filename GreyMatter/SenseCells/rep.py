import speech_recognition as sr
import os
import sys

# obtain audio from mic
r = sr.Recognizer()


# defining TTS
def tts(message):
    """
    This function takes message as an argument and converts it to speech depending on OS
    """
    if sys.platform == 'darwin':
        tts_engine = 'say'
    return os.system(tts_engine + ' ' + message)


tts("Hi there, i am chromium,how can i help you today")  # converts text to speech

# taking input from mic

with sr.Microphone() as source:
    print("Say Something!")
    audio = r.listen(source)
# Recognize speech with wit.ai

# with open ("recording.wav","wb") as f:
# f.write(audio.get_wav_data())
WIT_AI_KEY = "N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ"

try:
    speech_text = r.recognize_wit(audio, key="N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ").lower().replace("'", "")
    print("wit.ai thinks you said: " + r.recognize_wit(audio, key="N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ"))
    tts(speech_text)

except sr.UnknownValueError:

    print("Ariwn didn't understand you")

except sr.RequestError as e:
    print("could not request result from wit.ai Service;{0}".format(e))
