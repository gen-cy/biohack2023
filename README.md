# EIDA - Enhanced Intelligent Diagnostic Assistant

### Requirements to run
#### Basic requirements:
[Python](https://www.python.org/downloads/)(version 3 or later), [OpenAI account](https://platform.openai.com/signup?launch), [Azure subscription](https://azure.microsoft.com/free/cognitive-services), code from this [repository](https://github.com/gen-cy/biohack2023.git)
#### Initial installation/requirements:
1. Run this command to install the [Speech SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-sdk)
```
pip install azure-cognitiveservices-speech
```
2. Install [guidance](https://github.com/microsoft/guidance):
```
pip install guidance
```
3. Install [deep-translator](https://pypi.org/project/deep-translator/):
```
pip install deep-translator
```
4. Ensure the OpenAI key exists at `~/.openai_api_key` or is set as an environment variable.

Note that `libssl1.1` needs to be installed on Ubuntu 22.04. See [here](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-csharp&tabs=linux%2Cubuntu%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi) for more details: 
### Configuration:
1. First, go ahead and create a [Speech resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices)
2. Next you need to [get the Keys](https://learn.microsoft.com/en-GB/azure/cognitive-services/cognitive-services-apis-create-account#get-the-keys-for-your-resource) from your speech resource and set up your environment variables  
 You can set up the keys with the following commands: \
For windows:
```
setx SPEECH_KEY your-key
setx SPEECH_REGION your-region
```
For Linux/macOS:
```
export SPEECH_KEY=your-key
export SPEECH_REGION=your-region
```

### Run:
try out E.I.D.A. by running the following command in terminal:
```
python testing.py
```
Then follow the prompts provided by E.I.D.A.

### Demo links:
E.I.D.A - English | [Link](https://youtu.be/kFi7jlWCuCQ) \
E.I.D.A - Hindi | [Link](https://youtu.be/t8dOekdZZZo)
