from Cars import *
from CustomExc import *


try:
    car1 = Car("Station Wagon", 7253310,"5ЕЕ601")
except Exception as e:
    print(e.message)
try:
    car2 = Car("Station Wagon", 725310,"7ЩЗ312")
except Exception as e:
    print(e.message)
try:
    car2 = Car("Station Wagon", 9617521,"5")
except Exception as e:
    print(e.message)

