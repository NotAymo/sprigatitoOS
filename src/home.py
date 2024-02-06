import time

print("ooo-------SprigatitoOS--------ooo")
print("- [Settings]")
print("- Browser")
print("- About")
print("- Help")
print("- Store")
print("- Updates")
print("---------------------------------")
user_input = input("Launch an application.")
if user_input.lower() == "Settings":
    exec(open('src/settings.py').read())
else:
    user2_input = input("Application not found. Do you want to install it? [Yes/No]")
if user2_input.lower() == "Yes":
    exec(open('src/store.py').read())
else:
    exec(open('src/home.py').read())
