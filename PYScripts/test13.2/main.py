import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
disp = Dispatcher(bot,storage=MemoryStorage())

@disp.message_handler(commands=['start'])
async def start(msg):
    print('Привет! Я бот помогающий твоему здоровью.' )

@disp.message_handler()
async def all_messages(msg):
    print("Введите команду /start, чтобы начать общение")
if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True)