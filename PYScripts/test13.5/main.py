import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()

api = ""
bot = Bot(token = api)
disp = Dispatcher(bot,storage=MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row(KeyboardButton(text = "Информация"),KeyboardButton(text = "Рассчитать"))

@disp.message_handler(commands=['start'])
async def start(msg):
    await msg.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard )

@disp.message_handler(text = "Информация")
async def info(msg):
    await msg.answer("Этот бот используется для вычисления калорий. \n Нажмите \"Рассчитать\" или наишите Calories для начала вычислений", reply_markup=keyboard )

@disp.message_handler(text="Рассчитать")
async def set_age(msg):
    await msg.answer("Введите возраст",reply_markup=None)
    await UserState.age.set()
@disp.message_handler(state=UserState.age)
async def set_height(msg,state):
    await state.update_data(age = msg.text)
    await msg.answer('Введите рост')
    await UserState.height.set()
@disp.message_handler(state=UserState.height)
async def set_weight(msg,state):
    await state.update_data(height = msg.text)
    await msg.answer('Введите массу')
    await  UserState.weight.set()
@disp.message_handler(state=UserState.weight)
async def get_calories(msg,state):
    await state.update_data(weight = msg.text)
    data = await state.get_data()
    result =10 * float(data['weight']) + 6.25 * float(data['height']) - 5 * float(data['age']) + 5
    await msg.answer(f"Норма калорий: {result}")
    await state.finish()

@disp.message_handler()
async def all_messages(msg):
    if msg['text'].lower() == 'lorem':
        await msg.answer("ipsum")
        return 0
    await msg.answer("Введите команду /start, чтобы начать общение")
if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True)