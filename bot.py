import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from ChatGPT_function import ChatGPT

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

GPT_TOKEN = os.getenv('GPT_TOKEN')


@dp.message_handler(commands='gpt')
async def gpt_talk(message: Message):
    prompt = ' '.join(message.text.split()[1:])
    answer_from_gpt = ChatGPT(prompt, GPT_TOKEN)
    await message.reply(answer_from_gpt)


if __name__ == '__main__':
    executor.start_polling(dp)
