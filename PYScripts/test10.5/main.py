import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name,'r',encoding="utf-8") as file:
        for line in file:
            if line != None:
                all_data.append(line)

    return all_data



if __name__ == '__main__':
    timestart = datetime.now()
    read_info("file_1.txt")
    read_info("file_2.txt")
    read_info("file_3.txt")
    read_info("file_4.txt")
    timestop = datetime.now()
    timeres = timestop - timestart
    print("Затрачено времени линейными вызовами")
    print(timeres)

    timestart = datetime.now()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(read_info,["file_1.txt","file_2.txt","file_3.txt","file_4.txt"])
        process.close()
        process.join()
    timestop = datetime.now()
    timeres = timestop - timestart
    print("Затрачено времени мультипроцессорными вызовами")
    print(timeres)
