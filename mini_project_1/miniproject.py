#!/usr/bin/env python3
print("ello!")
print("Did you say, hello?")
print("No, I said ello, but that\'s close enough.")

while True:
    num = input("choose a number between 1 and 10\n>")
    if num.isdigit():
        num = int(num)
        print(100 / num)
        break
    else:
        print("pick a number, dumm!")
