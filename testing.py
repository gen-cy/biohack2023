import guidance
import re
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")
guidance.llm.cache.clear()

prompt = guidance(
'''{{#system~}}
You are a chatbot designed to talk to people who are have some medical concerns they want addressed.
Extract information about onset, location, duration, characteristics, aggravating factors, relieveing factors, timing, and severity of what the person is feeling. 
This is not to provide suggestions on what the person can do, but the information will be passed to a primary healthcare provider to follow up with the patient. 
Ask for clarifications in a simple manner. Keep the messages clear and consise. Do not ask for multiple responses from the user at once.
When prompted 'GENERATE HPI' generate a history of present illness for the patient.
{{~/system}}
{{~#geneach 'conversation' stop=False}}
{{#user~}}
{{set 'this.user_text' (await 'user_text')}}
{{~/user}}
{{#assistant~}}
{{gen 'this.ai_text' temperature=0 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}''')
print("What is the purpose of your visit today?\n")
while True:
    user_input = input("User: ")
    # prompt= prompt(user_text ='Remember these three things in my list: water and ice.')
    prompt = prompt(user_text = str(user_input))
    # print(prompt)

    prompt['conversation']
    # prompt = prompt(user_text = 'What is in my list?')
    print(prompt)