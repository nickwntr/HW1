import io
from pathlib import Path

def custom_write(file_name,*strings):
    with Path(file_name) as plist:
        if not plist.exists():
            nfile = open(file_name, 'w')
            nfile.close()

    strings_positions = {}
    reader = open(file_name, 'r',encoding="utf-8")
    for stradd in strings:
        reader = open(file_name, 'r', encoding="utf-8")
        lcount = len(reader.readlines()) + 1
        reader = open(file_name, 'a',encoding="utf-8")
        strings_positions[(lcount,reader.tell())] = stradd
        reader.write(f"{stradd} \n")
    reader.close()
    return strings_positions

result = custom_write("logs.txt","str1","lorem","amesno")
print(result)