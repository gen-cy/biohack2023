# Biohack 2023 Project

## Install

### OpenAI

First install `guidance`:

`pip install guidance`

Ensure the OpenAI key exists at `~/.openai_api_key` or is set as an environment variable.

### Azure Cognitive Speech Services

Install `azure-cognitiveservices-speech`

`pip install azure-cognitiveservices-speech`

Note that `libssl1.1` needs to be installed on Ubuntu 22.04. See [here](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-csharp&tabs=linux%2Cubuntu%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi) for more details: 