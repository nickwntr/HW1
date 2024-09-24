
import asyncio
import random

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования. Сила:{power}")
    for i in range(0,6):
        await asyncio.sleep(50/power)
        print(f"Силач {name} поднял шар {i+1}")
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    contestans = []
    for i in range(3):
        contestans.append(asyncio.create_task(
            start_strongman(f"Strongman # {i + 1}", random.randint(10, 70))))
    for contestant in contestans:
        await contestant

asyncio.run(start_tournament())