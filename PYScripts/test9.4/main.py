from random import choice

class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x,y: True if x == y else False,first,second))
print(result)


def get_advanced_writer(file_name):
    def write_anything(*data_set):
        with open(file_name,"a",encoding="utf-8") as file:
            file.write('\n'.join(str(i) for i in data_set))
        file.close()
    return write_anything

write = get_advanced_writer('writehere.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

eightball = MysticBall("Да","Нет","Наверное")

print(eightball())
print(eightball())
print(eightball())