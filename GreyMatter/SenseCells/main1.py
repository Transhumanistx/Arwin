import sys
import os
import yaml
import pyvona

import speech_recognition as sr


# defining TTS
def tts(message):
    """
    This function takes message as an argument and converts it to speech depending on OS
    """
    tts_engine = pyvona.create_voice()
    tts_engine.voice_name = 'Joey'
    if sys.platform == 'darwin':
        tts_engine = 'say'
    return os.system(tts_engine + ' ' + message)


# setting up the variable
name = "Transhumanistx"
tts('Welcome ' + name + ', your systems are now ready to run,How can I help you?')
WIT_AI_KEY = "N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ"


def main():
    # obtain audio from mic
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)
    # Recognize speech with wit.ai
    # with open ("recording.wav","wb") as f:
    # f.write(audio.get_wav_data())
    tts_engine.voice_name = 'Joey'
    tts_engine.speak(message)

    try:
        speech_text = r.recognize_wit(audio, key="N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ").lower().replace("'", "")
        print("Chromium thinks you said: " + speech_text)

    except sr.UnknownValueError:
        print("Chromium didn't understand you")

    except sr.RequestError as e:
        print("could not request result from wit.ai Service;{0}".format(e))

    tts(speech_text)


main()
