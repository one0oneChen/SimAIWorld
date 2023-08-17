"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling OpenAI APIs.

TODO:
    1.展示页面大小-done
    2.展示界面汉化-done
        - 人物状态汉化
        - 人物名称汉化
        - 系统状态汉化-done
    3.Django前端转发
"""
import json
import os
import random
import openai
import time
from reverie.backend_server.utils import *

openai.api_key = random.choice(openai_api_key)
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "https://127.0.0.1:7890"


def ChatGPT_request(prompt):
    """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response.
  ARGS:
    prompt: a str prompt
    gpt_parameter: a python dictionary with the keys indicating the names of
                   the parameter and the values indicating the parameter
                   values.
  RETURNS:
    a str of GPT-3's response.
  """
    time.sleep(1)

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ChatGPT ERROR:{e}"


prompt = """
---
Character 1: Maria Lopez is working on her physics degree and streaming games on Twitch to make some extra money. She visits Hobbs Cafe for studying and eating just about everyday.
Character 2: Klaus Mueller is writing a research paper on the effects of gentrification in low-income communities.

Past Context: 
138 minutes ago, Maria Lopez and Klaus Mueller were already conversing about conversing about Maria's research paper mentioned by Klaus This context takes place after that conversation.

Current Context: Maria Lopez was attending her Physics class (preparing for the next lecture) when Maria Lopez saw Klaus Mueller in the middle of working on his research paper at the library (writing the introduction).
Maria Lopez is thinking of initating a conversation with Klaus Mueller.
Current Location: library in Oak Hill College

(This is what is in Maria Lopez's head: Maria Lopez should remember to follow up with Klaus Mueller about his thoughts on her research paper. Beyond this, Maria Lopez doesn't necessarily know anything more about Klaus Mueller) 

(This is what is in Klaus Mueller's head: Klaus Mueller should remember to ask Maria Lopez about her research paper, as she found it interesting that he mentioned it. Beyond this, Klaus Mueller doesn't necessarily know anything more about Maria Lopez) 

Here is their conversation. 

Maria Lopez: "
---
Output the response to the prompt above in json. The output should be a list of list where the inner lists are in the form of ["<Name>", "<Utterance>"]. Output multiple utterances in ther conversation until the conversation comes to a natural conclusion.
Example output json:
{"output": "[["Jane Doe", "Hi!"], ["John Doe", "Hello there!"] ... ]"}
"""


def test():
    print(ChatGPT_request(prompt))


if __name__ == "__main__":
    test()
