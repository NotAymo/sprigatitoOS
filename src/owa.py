import time

print("Welcome to SprigatitoOS !")
name = input("Username:") 
print("Hello " + name, "! Welcome to SprigatitoOS")
time.sleep(2)
exec(open('src/home.py').read())

