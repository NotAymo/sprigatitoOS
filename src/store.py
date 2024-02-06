import time

print("|SprigatitoOS Store----------------------------[_][][X]|")
print("|   [Home]   |      Welcome to SprigatitoOS Store!     |")
print("|   Search   |     Install more apps for more content! |")
print("|------------|                                         |")
print("|-Categories-|                                         |")
print("|     Fun    |                                         |")
print("|     Dev    |                                         |")
print("|(i) Info    |                                         |")
print("--------------------------------------------------------")
user_input = input("Choose a category")
if user_input.lower() == "Search":
    exec(open('src/lib/storesearch.py').read())
