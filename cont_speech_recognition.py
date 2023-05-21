import azure.cognitiveservices.speech as speechsdk
import time
import json

speech_key, service_region = "dde0c05202fc418d861b62b6ea122128","westus"
weatherfilename="en-us_zh-cn.wav"

# Currently the v2 endpoint is required. In a future SDK release you won't need to set it. 
endpoint_string = "wss://{}.stt.speech.microsoft.com/speech/universal/v2".format(service_region)
translation_config = speechsdk.translation.SpeechTranslationConfig(
    subscription=speech_key,
    endpoint=endpoint_string,
    speech_recognition_language='en-US',
    target_languages=('de', 'fr'))
audio_config = speechsdk.audio.AudioConfig(filename=weatherfilename)

# Set the LanguageIdMode (Optional; Either Continuous or AtStart are accepted; Default AtStart)
translation_config.set_property(property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode, value='Continuous')

# Specify the AutoDetectSourceLanguageConfig, which defines the number of possible languages
auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["en-US", "de-DE", "zh-CN"])

# Creates a translation recognizer using and audio file as input.
recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=translation_config, 
    audio_config=audio_config,
    auto_detect_source_language_config=auto_detect_source_language_config)

def result_callback(event_type, evt):
    """callback to display a translation result"""
    print("{}: {}\n\tTranslations: {}\n\tResult Json: {}".format(
        event_type, evt, evt.result.translations.items(), evt.result.json))

done = False

def stop_cb(evt):
    """callback that signals to stop continuous recognition upon receiving an event `evt`"""
    print('CLOSING on {}'.format(evt))
    # nonlocal done
    # done = True
    done[0] = True  # Modify the value of `done` using the mutable object

# connect callback functions to the events fired by the recognizer
recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
# event for intermediate results
recognizer.recognizing.connect(lambda evt: result_callback('RECOGNIZING', evt))
# event for final result
recognizer.recognized.connect(lambda evt: result_callback('RECOGNIZED', evt))
# cancellation event
recognizer.canceled.connect(lambda evt: print('CANCELED: {} ({})'.format(evt, evt.reason)))

# stop continuous recognition on either session stopped or canceled events
recognizer.session_stopped.connect(stop_cb)
recognizer.canceled.connect(stop_cb)

def synthesis_callback(evt):
    """
    callback for the synthesis event
    """
    print('SYNTHESIZING {}\n\treceived {} bytes of audio. Reason: {}'.format(
        evt, len(evt.result.audio), evt.result.reason))
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("RECOGNIZED: {}".format(evt.result.properties))
        if evt.result.properties.get(speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult) == None:
            print("Unable to detect any language")
        else:
            detectedSrcLang = evt.result.properties[speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult]
            jsonResult = evt.result.properties[speechsdk.PropertyId.SpeechServiceResponse_JsonResult]
            detailResult = json.loads(jsonResult)
            startOffset = detailResult['Offset']
            duration = detailResult['Duration']
            if duration >= 0:
                endOffset = duration + startOffset
            else:
                endOffset = 0
            print("Detected language = " + detectedSrcLang + ", startOffset = " + str(startOffset) + " nanoseconds, endOffset = " + str(endOffset) + " nanoseconds, Duration = " + str(duration) + " nanoseconds.")
            global language_detected
            language_detected = True

# connect callback to the synthesis event
recognizer.synthesizing.connect(synthesis_callback)

# start translation
recognizer.start_continuous_recognition()

while not done:
    time.sleep(.5)

recognizer.stop_continuous_recognition()