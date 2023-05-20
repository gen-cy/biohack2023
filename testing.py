import guidance
import re
guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")
guidance.llm.cache.clear()

prompt = guidance(
'''{{#system~}}
You are a helpful assistant
{{~/system}}
{{~#geneach 'conversation' stop=False}}
{{#user~}}
{{set 'this.user_text' (await 'user_text')}}
{{~/user}}
{{#assistant~}}
{{gen 'this.ai_text' temperature=0 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}''')
while True:
    user_input = input("User: ")
    # prompt= prompt(user_text ='Remember these three things in my list: water and ice.')
    prompt = prompt(user_text = str(user_input))
    # print(prompt)

    prompt['conversation']
    # prompt = prompt(user_text = 'What is in my list?')
    print(prompt)