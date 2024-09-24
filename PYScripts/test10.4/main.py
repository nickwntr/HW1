from serviceconomy import *
from threading import Thread


tables = [Table(i) for i in range(1,5)]
guest_names = ["Nick", "Simeon", "Oleg", "Valya", "Ibragim","Sara", "Klara"]
guests = [Guest(name) for name in guest_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

