import os
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone(from_lang="en-US"):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language = from_lang

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    input("\tHit enter when ready to talk: ")

    print("\tSpeak into your microphone.")
    
    # Create an empty list to store recognized text
    recognized_text = []

    # Event handler for speech recognition
    def speech_recognized_callback(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            # print("Recognized: {}".format(evt.result.text))
            # Add recognized text to the list
            recognized_text.append(evt.result.text)

    # Connect the event handler
    speech_recognizer.recognized.connect(speech_recognized_callback)
    
    # Start continuous recognition
    speech_recognizer.start_continuous_recognition()

    input("\tPress Enter to stop listening...")

    # Stop recognition
    speech_recognizer.stop_continuous_recognition()

    # Convert the list of recognized text into a single string
    result = " ".join(recognized_text)

    return result

# text = recognize_from_microphone()
# print("Printing transcribed text now:\n")
# print(text)
