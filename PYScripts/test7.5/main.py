import os
import time

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        try:
            filepath = os.path.join(root,file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = root
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        except:
            print("Файл не прочитан")