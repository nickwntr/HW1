from Wordsfinder import *

WF = WordsFinder("lorem.txt","ipsum.txt")
print(WF.get_all_words())
print(WF.find("text"))
print(WF.find("ipsum"))
print(WF.find("beta"))
print(WF.count("text"))
print(WF.count("ipsum"))
print(WF.count("beta"))
