calls = 0


def countcalls():
    global calls
    calls += 1


def string_info(string):
    countcalls()
    print((len(string), string.upper(), string.lower()))


def is_contains(string, list_to_search):
    countcalls()
    for item in list_to_search:
        if item.lower().find(string.lower()) >= 0:
            return True
    return False

string_info("AlpHA")
string_info("BRavO")
print(is_contains("c",["Charlie","Delta","Epsilon"]))
print(is_contains("p",["Fal","Gem","sfgggg"]))
print(calls)
