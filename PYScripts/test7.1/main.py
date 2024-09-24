from Classes import *
magnit = Shop()
magnit.add(Product("Potato",70,"Vegetaples"),
           Product("Apple",12,"Fruits"))
magnit.get_products()
magnit.add(Product("Potato",11,"Vegetaples"),
           Product("Apple",189,"Fruits"))
magnit.get_products()