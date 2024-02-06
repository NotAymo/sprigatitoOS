import platform
import time

name = input("Username:") 
print("|SprigatitoOS Settings------------[_][][X]")
print("|[ABOUT]   |      SprigatitoOS           |")
print("| User     |     OS Version: 1           |")
print("|          |    CPU: " + platform.processor(), "             |")
print("|          |    GPU: Not Found           |")
print("------------------------------------------")
user_input = input("Choose a setting:")
if user_input.lower() == "User":
    print("|SprigatitoOS Settings------------[_][][X]")
    print("| ABOUT   |             [User]           |")
    print("| [User]  |     Username: " + name, "    |")
    print("|         |     Root: Null               |")
    print("------------------------------------------")
else:
    print("This category/setting is not found.")
