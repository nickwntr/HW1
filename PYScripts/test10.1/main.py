from time import sleep
from threading import Thread
from datetime import datetime



def write_words(word_count,file_name):
    creator = open(file_name,"w")
    creator.close()
    with open(file_name,"a",encoding="utf-8") as file:
        for i in range(word_count+1):
            file.write(f"Какое-то слово № {i} \n")
            sleep(0.1)
    print(f"Запись в файл {file_name} завершена")


thread1 = Thread(target=write_words, args=[50,"file1.txt"])
thread2 = Thread(target=write_words, args=[20,"file2.txt"])
thread3 = Thread(target=write_words, args=[70,"file3.txt"])
timestart = datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
timestop = datetime.now()
timeres = timestop - timestart
print("Потрачено времени на потоки")
print(timeres)
timestart = datetime.now()
write_words(50,"file4.txt")
write_words(20,"file5.txt")
write_words(70,"file6.txt")
timestop = datetime.now()
timeres = timestop - timestart
print("Потрачено времени на вызовы функцции")
print(timeres)
