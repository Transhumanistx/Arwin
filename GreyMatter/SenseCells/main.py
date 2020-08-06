import speech_recognition as sr

# obtain audio from mic
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something!")
    audio = r.listen(source)
# Recognize speech with wit.ai
# with open ("recording.wav","wb") as f:
WIT_AI_KEY = "N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ"
# f.write(audio.get_wav_data())
try:
    print("wit.ai thinks you said: " + r.recognize_wit(audio, key="N72BBACKYBSIJMYWAGR7E46SWH5P7PFQ"))

except sr.UnknownValueError:

    print("Ariwn didn't understand you")

except sr.RequestError as e:
    print("could not request result from wit.ai Service;{0}".format(e))
