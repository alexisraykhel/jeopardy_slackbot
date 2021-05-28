from json import load
from random import choice

#https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/

with open(f"JEOPARDY_QUESTIONS1.json", "r") as f:
    all_questions = load(f)

print("questions loaded!")

# this really needs to be a df, because this is terrible
# something like: dfItem = pd.DataFrame.from_records(list of json data)


qs_by_value = {'200': [x for x in all_questions if x['value'] == '$200'],
               '400': [x for x in all_questions if x['value'] == '$400'],
               '600': [x for x in all_questions if x['value'] == '$600'],
               '800': [x for x in all_questions if x['value'] == '$800'],
               '1000': [x for x in all_questions if x['value'] == '$1000'],
               '1200': [x for x in all_questions if x['value'] == '$1200'],
               '1400': [x for x in all_questions if x['value'] == '$1400'],
               '1600': [x for x in all_questions if x['value'] == '$1600'],
               '1800': [x for x in all_questions if x['value'] == '$1800'],
               '2000': [x for x in all_questions if x['value'] == '$2000']
               }

# need other question difficulties

""" {"category": "HISTORY", 
"air_date": "2004-12-31", 
"question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'", 
"value": "$200", 
"answer": "Copernicus", 
"round": "Jeopardy!", 
"show_number": "4680"}"""

import os

from slack import RTMClient

# This event runs when the connection is established and shows some connection info
@RTMClient.run_on(event="open")
def show_start(**payload):
    print(payload)


@RTMClient.run_on(event="message")
def jbot(**payload):
    data = payload["data"]
    web_client=payload['web_client']
    bot_id=data.get("bot_id", "")

    if bot_id == "":
        channel_id = data["channel"]

        #Extract message
        text = data.get("text", "")
        text = text.split(">")[-1].strip()

        if "jbot" in text:
            split = text.split(" ")
            money = split[1]
            print("type money", type(money))

            print("split", split, "money", money)

            if str(money) in qs_by_value:
                print("Yes")
                one_question = choice(qs_by_value.get(str(money)))
            else:
                print("NO")
                one_question = choice(all_questions)
                money = one_question['value']
            print("post ifs")
            print("ONE QUESTION:", one_question)
            category = one_question['category']
            print("Cat", category)
            the_q = one_question['question']
            print("Q", the_q)
            response = f"Welcome to Jeopardy! For {str(money)} in the category {category}:\n{the_q}"
            print("New response", response)
            web_client.chat_postMessage(channel=channel_id, text=response)
            print("why not?")

        else:
            print("are we passing?")
            pass


try:
    rtm_client = RTMClient(token=os.environ['SLACK_BOT_TOKEN'])
    print("Go bot go!")
    rtm_client.start()
except Exception as e:
    print("hey")
    print(e)

#TODO: respond to user answer using slack RTMClient
#TODO: add seen/not seen flag
#TODO: check category/answer potentially (fuzzywuzzy)
#TODO: error handling from bot if it gets unexpected input
#TODO: handle time out/don't time out?

#TODO: host it