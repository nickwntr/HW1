import chivalry
import random
threads = []
for i in range(7):
    thread = chivalry.Knight(f"Sir Mullich the {i+1}",random.randint(5,25))
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()