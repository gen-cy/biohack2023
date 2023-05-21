import guidance
import re
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")
guidance.llm.cache.clear()

# test_text = """
# <|im_start|>system
# You are a chatbot designed to talk to 
# people who have some medical concerns they 
# want addressed.
# Extract information about onset, location, 
# duration, characteristics, aggravating 
# factors, relieveing factors, timing, and 
# severity of what the user is feeling 
# through the use of "OLD CARTS" is a 
# mnemonic device that assists clinicians in 
# remembering the pertinent questions to ask 
# while assessing an individual’s present 
# illness. When a user presents to their 
# clinician with complaints of a new or 
# reoccurring medical problem, the clinician 
# may use "OLD CARTS" as a structured 
# guideline and framework from which they 
# will ask questions and collect information 
# before they perform a physical exam. Most 
# commonly, "OLD CARTS" can be utilized for a 
# user who is experiencing pain, however, 
# this mnemonic can be used as a framework 
# for any presenting symptom. 
# Do not state more than one question.
# Do not explicitly say or use OLD CARTS, 
# rather implement OLD CARTS to work together 
# with the user.
# You do not know the user's illness or 
# sickness.
# This is not to provide suggestions on what 
# the user can do, but the information will 
# be passed to a primary healthcare provider 
# to follow up with the user. 
# Ask for clarifications in a simple manner. 
# Keep the messages clear and consise. Do not 
# ask for multiple responses from the user at 
# once.
# Ask questions throughout the conversation 
# that might help expose their medical 
# concerns.
# Ask only one question at a time.
# When prompted 'GENERATE HPI' generate a 
# history of present illness for the user.
# Do not ask the user if they would like a 
# history of present illness generated for 
# them.
# You start with the prompt: What symptoms or 
# medical concerns are you experiencing 
# today?<|im_end|>
# <|im_start|>user
# Reply to this response
# My head hurts. The pain is around my 
# foreheand is exacerbated by bright lights. 
# Drinking water helps alleviate the pain. It 
# seems to occur at random. It began around 
# last week. I would rate the pain at at an 8 
# out of 10. It is more of a sharp pain.
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for sharing that information with 
# me. Can you tell me more about the onset of 
# the pain? When did you first notice 
# it?<|im_end|>

# <|im_start|>user
# Reply to this response
# about lastw eek
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for letting me know. Can you 
# describe the location of the pain? Is it 
# only around your forehead or does it spread 
# to other areas of your head?<|im_end|>

# <|im_start|>user
# Reply to this response
# it is around my forehead
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for clarifying that. Can you 
# describe the duration of the pain? How long 
# does it usually last when it 
# occurs?<|im_end|>

# <|im_start|>user
# Reply to this response
# lasts for a few hours
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for sharing that information. Can 
# you describe the characteristics of the 
# pain? Is it a dull ache or a sharp 
# pain?<|im_end|>

# <|im_start|>user
# Reply to this response
# sharp 
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for letting me know. Can you tell 
# me more about what makes the pain worse? 
# Are there any specific activities or 
# factors that seem to trigger the 
# pain?<|im_end|>

# <|im_start|>user
# Reply to this response
# exercising makes it worse. sleeping helps 
# it to go away
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for sharing that information. Can 
# you tell me more about what makes the pain 
# better? You mentioned that drinking water 
# helps alleviate the pain, are there any 
# other things that help to relieve the 
# pain?<|im_end|>

# <|im_start|>user
# Reply to this response
# no
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for letting me know. Can you tell 
# me more about the timing of the pain? Does 
# it occur at a specific time of day or is it 
# random?<|im_end|>

# <|im_start|>user
# Reply to this response
# random
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Thank you for sharing that information. 
# Based on what you've told me, I would like 
# to generate a history of present illness 
# (HPI) for you. Please let me know if you 
# would like me to proceed.<|im_end|>

# <|im_start|>user
# Reply to this response
# Please generate the HPI.
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# <|im_start|>assistant
# Here is the history of present illness 
# (HPI) based on the information you 
# provided:

# The patient reports experiencing sharp pain 
# around their forehead that began around 
# last week. The pain lasts for a few hours 
# and occurs at random. The pain is 
# exacerbated by bright lights and 
# exercising. Drinking water helps alleviate 
# the pain, but there are no other relieving 
# factors. The patient rates the pain at an 8 
# out of 10 in terms of severity. The pain is 
# more of a sharp pain and is located around 
# the forehead. Sleeping helps the pain to go 
# away.

# Based on this information, it is 
# recommended that you schedule an 
# appointment with your primary healthcare 
# provider to further evaluate your symptoms 
# and determine the appropriate course of 
# treatment.<|im_end|>

# <|im_start|>user
# Reply to this response
# {{set 'conversation[-1].user_text' (await 
# 'user_text')}}
# by implementing OLD CARTS methods to better 
# understand the user's illness.<|im_end|>
# {{#assistant~}}
# {{gen 'conversation[-1].ai_text' 
# temperature=0 max_tokens=300}}
# {{~/assistant}}
# {{~#geneach 'conversation' stop=False}}
# {{#user~}}
# Reply to this response
# {{set 'this.user_text' (await 
# 'user_text')}}
# by implementing OLD CARTS methods to better 
# understand the user's illness.
# {{~/user}}
# {{#assistant~}}
# {{gen 'this.ai_text' temperature=0 
# max_tokens=300}}
# {{~/assistant}}
# {{~/geneach}}


# """

# Define the pattern
# asst_pattern = r'\<\|im_start\|\>assistant\n(.*)\<\|im_end\|\>'

hpi_pattern = r'\(HPI\) |  history of present illness'

# asst_output = []
# asst_matches = re.findall(asst_pattern, str(test_text))
# for match in asst_matches:
#     # print("INSIDE INSIDE INSIDE ------------")
#     # print(match)
#     asst_output.append(match)
# print("printing response")
# print(asst_output, "\n")

asst_pattern = r"(\<\|im_start\|\>assistant[\s\S]*?\<\|im_end\|\>)"

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
You are a chatbot designed to talk to people who have some medical concerns they want addressed.
Extract information about onset, location, duration, characteristics, aggravating factors, relieveing factors, timing, and severity of what the user is feeling through the use of "OLD CARTS" is a mnemonic device that assists clinicians in remembering the pertinent questions to ask while assessing an individual’s present illness. When a user presents to their clinician with complaints of a new or reoccurring medical problem, the clinician may use "OLD CARTS" as a structured guideline and framework from which they will ask questions and collect information before they perform a physical exam. Most commonly, "OLD CARTS" can be utilized for a user who is experiencing pain, however, this mnemonic can be used as a framework for any presenting symptom. 
Do not state more than one question.
Do not explicitly say or use OLD CARTS, rather implement OLD CARTS to work together with the user.
You do not know the user's illness or sickness.
This is not to provide suggestions on what the user can do, but the information will be passed to a primary healthcare provider to follow up with the user. 
Ask for clarifications in a simple manner. Keep the messages clear and consise. Do not ask for multiple responses from the user at once.
Ask questions throughout the conversation that might help expose their medical concerns.
Ask only one question at a time.
When prompted 'GENERATE HPI' generate a history of present illness for the user.
Do not ask the user if they would like a history of present illness generated for them.
You start with the prompt: What symptoms or medical concerns are you experiencing today?
{{~/system}}
{{~#geneach 'conversation' stop=False}}
{{#user~}}
Reply to this response
{{set 'this.user_text' (await 'user_text')}}
by implementing OLD CARTS methods to better understand the user's illness.
{{~/user}}
{{#assistant~}}
{{gen 'this.ai_text' temperature=0 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}''')
print("What symptoms or medical concerns are you experiencing today?\n")

while True:
    user_input = input("User: ")
    asst_output = []
    # prompt= prompt(user_text ='Remember these three things in my list: water and ice.')
    prompt = prompt(user_text = str(user_input))
    # print(prompt)

    # prompt['conversation']
    # prompt = prompt(user_text = 'What is in my list?')
    asst_matches = re.findall(asst_pattern, str(prompt))
    hpi_matches = re.findall(hpi_pattern, str(prompt))
    for match in hpi_matches:
        print("check for hpi match")
        # if match == "(HPI)":
        print("hpi match")
        prompt = prompt(user_text = "Please generate the HPI.")
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

    for match in asst_matches:
        # print("INSIDE INSIDE INSIDE ------------")
        # print(match)
        asst_output.append(match)
    print("printing response")
    print(asst_output[-1], "\n")
    # print()
    # print(prompt)

