#!/usr/bin/env python3
import textwrap

counter = 0
value_check = 0

question_bank = [
    {"question":"Which of these potato products do you most identify with?",
    "option_1":"1: A bumpy russet potato.",
    "option_2":"2: Cajun tater tots.",
    "option_3":"3: Week old McDonald's french fries that fell under a car seat.",},

    {"question":"You lent a friend a huge sum of money before they left on an adventure. They’ve now returned with a small fortune. How do you approach the topic of the loan?",
    "option_1":"1: Wait until they’ve had a chance to recover from their trip before bringing it up over second breakfast.",
    "option_2":"2: No need. You had them sign a contract with clear repayment details.",
    "option_3":"3: Forcibly take the fortune, seeing it as a return on investment.",},
    
    {"question":"You come across a scroll that allows you to cast a spell of invisibility on yourself for one day. What do you do with it?",
    "option_1":"1: Lock it away, its to dangerous for just anyone to find.",
    "option_2":"2: Use your newfound stealth to sneak into a bank and make off with all the money you can carry.",
    "option_3":"3: Use the scroll to tickle your manager for a day.",},

    {"question":"You witness a brawl in the streets; One of the fighters dies and is carted away. His coin purse was left behind in the commotion, and nobody but you seems to have noticed. What do you do?",
    "option_1":"1: Attempt to find the person's family and return the gold to them.",
    "option_2":"2: Leave the coins and go about your day. Its not your business.",
    "option_3":"3: Invest the coins into crypto and contemplate your future fortune.",},

    {"question":"Oops, you died... What should be inscribed on the monument dedicated to your life?",
    "option_1":'1: “A gentle soul who changed the world."',
    "option_2":'2: "Go Away, Im Asleep"',
    "option_3":'3: “If you can read this, you are standing on my boobs"',},
]

input('''
#*********************************************************************#
#   Welcome to the conclusive and definitive moral alignment quiz!    #
#   You will be given five question_bank from the question bank       #
#   Based on how you respond, we'll find out if you are good or evil! #
#   ... And who your spirit character is!                             #
#*********************************************************************#
(press any key to continue):\n''')
print ("\n" * 100)

while counter <= 5:
    if counter == 5:
        if value_check <= 10:
            neutral_evil = "You see others as a means to an end. You only make friends and allies temporarily, and will turn on someone in a second if you can see a way to gain from it. You don’t really go out of your way to cause harm to others, but you don\'t really go out of your way to prevent it either.\n"

            print("You Got: Neutral Evil!\n")
            wrapper = textwrap.TextWrapper(width=70)
            word_list = wrapper.wrap(text=neutral_evil)
            for element in word_list:
                print(element)
            print("\nYour spirit character is Voldemort from Harry Potter\n")

        elif value_check <= 21:
            true_neutral = "You don’t feel strongly about much of anything. Frankly, you can take or leave a lot of things in your life. You’re mostly guided by instinct, rather than conscious decision.\n"

            print("You Got: True Neutral!\n")
            wrapper = textwrap.TextWrapper(width=70)
            word_list = wrapper.wrap(text=true_neutral)
            for element in word_list:
                print(element)
            print("\nYour spirit character is Uatu the Watcher from Marvel\n")

        elif value_check <= 30:
            neutral_good = "You are guided by your conscience, rather than any formal laws or traditions. You may occasionally break the rules, but it’s generally in service of the greater good.\n"

            print("You Got: Neutral Good!\n")
            wrapper = textwrap.TextWrapper(width=70)
            word_list = wrapper.wrap(text=neutral_good)
            for element in word_list:
                print(element)
            print("\nYour spirit character is Albus Dumbledore\n")

        elif value_check > 30:
            chaotic_evil = "If there's a pot, you're going to stir it. If there's a fire, you're going to add fuel to it. If there is calm, you are going to blow it all up. If there is something on an edge of a counter, you are going to push it off."

            print("You Got: Chaotic Evil!\n")
            wrapper = textwrap.TextWrapper(width=70)
            word_list = wrapper.wrap(text=chaotic_evil)
            for element in word_list:
                print(element)
            print("\nYour spirit character is Carnage from Marvel or a House Cat\n")
            
        else:
            print("hmm, something wrong here")
        break

    try:
        print(question_bank[counter]["question"] + "\n")
        print(question_bank[counter]["option_1"])
        print(question_bank[counter]['option_2'])
        print(question_bank[counter]['option_3'] + "\n")
    
        user_select = int(input("Enter: 1, 2, or 3: "))
        print ("\n" * 75)

        if user_select < 1 or user_select > 3:
            raise ValueError('Error: Your input should be 1, 2, or 3.') 
        counter += 1
        if user_select == 1:
            value_check += 1
        elif user_select == 2:
            value_check += 5
        elif user_select == 3:
            value_check += 10
        else:
            print("Oopsie Poopsie, wrong input")
    except:
        print("Apologies, You must type in a whole number: 1, 2, or 3 (inclusive).")
    
    print(f'Total Questions Answered: {counter}\n')