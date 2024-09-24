import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
disp = Dispatcher(bot,storage=MemoryStorage())

@disp.message_handler(commands=['start'])
async def start(msg):
    await msg.answer('Привет! Я бот помогающий твоему здоровью.' )

@disp.message_handler()
async def all_messages(msg):
    if msg['text'].lower() == 'lorem':
        await msg.answer("ipsum")
        return 0
    await msg.answer("Введите команду /start, чтобы начать общение")
if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True)