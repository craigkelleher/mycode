#!/usr/bin/python3

user_name = input("Please enter your name: ")
day = input("Please enter the day of the week: ")

# METHOD 1: CONCENATION
print("Hello, " + user_name +"! Happy " + day + "!")
# METHOD 2: FORMAT METHOD
print("Hello, {}! Happy {}!".format(user_name, day))
# METHOD 3: F-STRING <-- CHAD'S RECOMMENDATION
print(f"Hello, {user_name}! Happy {day}!")
