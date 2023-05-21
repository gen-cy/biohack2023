import guidance
import re
from text_to_speech import transcribe_to_speech
from speech_to_text import recognize_from_microphone
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")
guidance.llm.cache.clear()

# helpers

# need to fix lol
def strip_assistant(text):
    stripped_text = text.replace('\<\|im_start\|\>assistant', '').replace('\<\|im_end\|\>', '').replace('\n','')
    return stripped_text


# Define the pattern
# asst_pattern = r'\<\|im_start\|\>assistant\n(.*)\<\|im_end\|\>'

hpi_pattern = r'\(HPI\) |  history of present illness'
asst_pattern = r"(\<\|im_start\|\>assistant[\s\S]*?\<\|im_end\|\>)"

# ending regex pattern

end_text = r"Thank you, a healthcare provider will see you shortly."

# exit()
# essentially precharting
# valid only if done day of patient visit
# example usage: patient checks into hospital
#   while waiting for someone to meet, talk to this program
#   program can note information about patient's visit
#   for use when a PCP meets with them

# issues:

# generates HPI unprompted
#   perhaps catch w/regex and return message along lines of 'doctor will see you shortly'

prompt = guidance(
'''{{#system~}}
You are a chatbot designed to talk to patients who have some medical concerns they want addressed.
Ask the patient information about the onset, location, duration, characteristics, aggravating factors, relieveing factors, timing, and severity of what the user is feeling.
This is not to provide suggestions on what the user can do, but the information will be passed to a primary healthcare provider to follow up with the user. 
Do not ask the patient more than one question at a time.
Since you do not know the user's illness or sickness, ask qualifying questions about their problems.
Avoid repeating what the patient just said back to them.
If needed, ask for clarifications in a simple manner. Ask for these clarifications one at a time.
Once the information has been gathered, output this text word for word: 'Thank you, a healthcare provider will see you shortly.'
{{~/system}}
{{~#geneach 'conversation' stop=False}}
{{#user~}}
From the following prompt, extract information about the patient's problems to produce later:
{{set 'this.user_text' (await 'user_text')}}
{{~/user}}
{{#assistant~}}
{{gen 'this.ai_text' temperature=0.3 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}''')
initmsg = "What symptoms or medical concerns are you experiencing today?\n"
print(initmsg)
transcribe_to_speech(initmsg)

while True:
    # user_input = input("User: ")
    asst_output = []
    # user_text = str(user_input)
    user_input = str(recognize_from_microphone())
    print("\tUser said: {}".format(user_input))
    prompt = prompt(user_text = user_input)

    asst_matches = re.findall(asst_pattern, str(prompt))
    hpi_matches = re.findall(end_text, str(prompt))

    for match in asst_matches:
        # print("INSIDE INSIDE INSIDE ------------")
        # print(match)
        asst_output.append(match)

    msgtoprint = asst_output[-1][21:-10]
    print("printing response")
    print(msgtoprint)
    # response_msg = strip_assistant(asst_output[-1])
    # print(response_msg, "\n")
    transcribe_to_speech(msgtoprint)

    # hacky
    # exit prompt appears once as directive
    # begin exit condition if appears more than once
    if len(hpi_matches) > 1:
        for match in hpi_matches:
            print("check for hpi match")
            # if match == "(HPI)":
            print("hpi match")
            prompt = prompt(user_text = "Based on the information provided by the patient, generate a history of patient illness for a healthcare professional to review.")
            print("---\n{}\n---".format(prompt))
            hpi_matches = re.findall(asst_pattern, str(prompt))
            if hpi_matches:
                for hpi in hpi_matches:
                    asst_output.append(hpi)
            else:
                print("No history of present illness found.")
            # asst_matches = re.findall(asst_pattern, str(prompt))
            # for match_inner in asst_matches:
            #     asst_output.append(match_inner)


                # print(prompt)
                # exit()
            # print(asst_output[-1], "\n")
            print('---')
            print(asst_output[-1])
            exit()
    

