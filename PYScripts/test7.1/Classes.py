from pathlib import Path
from pprint import pprint


class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
class Shop:
    _file_name="products.txt"
    def __init__(self):
        with Path(self._file_name) as plist:
            if not plist.exists():
               creator = open(self._file_name,'w')
               creator.close()

    def get_products(self):
        file = open(self._file_name,'r')
        print(file.read())
        file.close()

    def add(self,*products):
        addr = open(self._file_name,'r')
        for product in products:
            if addr.read().find(str(product.name)) == -1:
                addr = open(self._file_name,'a')
                addr.write(f"{str(product)} \n")
                addr = open(self._file_name,'r')
                addr.seek(0)
            else:
                print(f"Продукт {str(product)} уже есть в магазине")
                addr.seek(0)
        addr.close()