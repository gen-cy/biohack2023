import os
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    
    # Set up a flag to track if there is silence for five seconds
    is_silence_detected = False
    
    # Event handler for speech recognition
    def speech_recognized_callback(evt):
        nonlocal is_silence_detected
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(evt.result.text))
            is_silence_detected = False
        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(evt.result.no_match_details))
            is_silence_detected = False
            
    # Event handler for silence detected
    def silence_detected_callback(evt):
        nonlocal is_silence_detected
        is_silence_detected = True
        print("Silence detected.")

    # Event handler for session stopped
    def session_stopped_callback(evt):
        nonlocal is_silence_detected
        # if is_silence_detected:
        #     print("Listening stopped due to five seconds of silence.")
        # else:
        #     print("Listening stopped.")
    
    # Connect event handlers
    speech_recognizer.recognized.connect(speech_recognized_callback)
    speech_recognizer.speech_end_detected.connect(silence_detected_callback)
    speech_recognizer.session_stopped.connect(session_stopped_callback)
    
    # Start continuous recognition
    speech_recognizer.start_continuous_recognition()

    input("Press Enter to stop listening...")

    # Stop recognition
    speech_recognizer.stop_continuous_recognition()

recognize_from_microphone()