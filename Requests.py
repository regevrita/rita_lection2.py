import os
from pprint import pprint

from ChatGPT_function import ChatGPT
from dotenv import load_dotenv



load_dotenv()
GPT_TOKEN = os.getenv('GPT_TOKEN')

def questions():
    user_input = input("Введите ваш вопрос:")
    answer = ChatGPT(text=user_input, token=GPT_TOKEN)
    pprint(answer)

questions()


