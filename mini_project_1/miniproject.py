#!/usr/bin/env python3

import textwrap
import os

def main():
    counter = 0
    morality_check = 0

    # Question dictionary to pull from and plop on the user's console window
    # with choosable options in the same dicitonary
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
    
    # Print welcome introduction to the user and clear the screen before/after
    os.system('clear')
    #print ("\n" * 100)
    input('''
    #*********************************************************************#
    #   Welcome to the conclusive and definitive moral alignment quiz!    #
    #   You will be given five questions from the question bank           #
    #   Based on how you respond, we'll find out if you are good or evil! #
    #   ... And who your spirit character is!                             #
    #*********************************************************************#
    (press Enter to continue):\n''')
    #print ("\n" * 100)
    os.system('clear')

    # Program will run until 5 questions have been answered
    while counter <= 5:
        # After 5 turns, the value check and determine user's alignment!
        if counter == 5:
            if morality_check <= 10:
                neutral_good = "You do good for goodness' sake, rather than being directed to by laws or by whim. You may obey the law or break it when you felt it would server a greater good. Your need to help others and reduce suffering takes precedence over all else.\n"
                
                print("You Got: Neutral Good!\n")
                # Format text string to be 70 characters wide and print to the screen
                word_list = textwrap.TextWrapper(width=70).wrap(text=neutral_good)
                for element in word_list:
                    print(element)
                print("\nYour spirit character is Albus Dumbledore from Harry Potter\n")

            elif morality_check <= 21:
                true_neutral = "You don't seem to have prejudice or compulsion. You either disregard any commitment to good, evil, law, and chaos, or belive that a balance is needed between these forces in the world. You simply do what seems natural to you, without feelings with regard to good versus evil, or order versus chaos.\n"

                print("You Got: True Neutral!\n")
                # Format text string to be 70 characters wide and print to the screen
                word_list = textwrap.TextWrapper(width=70).wrap(text=true_neutral)
                for element in word_list:
                    print(element)
                print("\nYour spirit character Han Solo from Star Wars\n")

            elif morality_check <= 30:
                neutral_evil = "You see others as a means to an end. You only make friends and allies temporarily, and will turn on someone in a second if you can see a way to gain from it. You are completely out for yourself and have no love of order or law and show no remorse for those hurt by your actions.\n"

                print("You Got: Neutral Evil!\n")
                # Format text string to be 70 characters wide and print to the screen
                word_list = textwrap.TextWrapper(width=70).wrap(text=neutral_evil)
                for element in word_list:
                    print(element)
                print("\nYour spirit character is Voldemort from Harry Potter\n")

            elif morality_check > 30:
                chaotic_evil = "If there's a pot, you're going to stir it. If there's a fire, you're going to add fuel to it. If there is calm, you are going to blow it all up. If there is something on an edge of a counter, you are going to push it off."

                print("You Got: Chaotic Evil!\n")
                # Format text string to be 70 characters wide and print to the screen
                word_list = textwrap.TextWrapper(width=70).wrap(text=chaotic_evil)
                for element in word_list:
                    print(element)
                print("\nYour spirit character is a House Cat\n")
                
            else:
                print("hmm, something wrong here")
            break
            
        # In the while loop, always attempt the following:
        try:
            # Output questions to the user
            word_list = textwrap.TextWrapper(width=70).wrap(text=question_bank[counter]["question"] + "\n")
            for element in word_list:
                print(element)
            print(question_bank[counter]["option_1"])
            print(question_bank[counter]['option_2'])
            print(question_bank[counter]['option_3'] + "\n")
            # Prompt user for response:
            user_select = int(input("Enter: 1, 2, or 3: "))
            # Clear screen after user response
            #print ("\n" * 100)
            os.system('clear')
            
            # Validate user input and raise a value error if incorrect input
            if user_select < 1 or user_select > 3:
                raise ValueError('Error: Your input should be 1, 2, or 3.')
            # Increment turn counter
            counter += 1
            # Calculate user morality with morality_check and update after every response
            if user_select == 1:
                morality_check += 1
            elif user_select == 2:
                morality_check += 5
            elif user_select == 3:
                morality_check += 10
            else:
                print("Oopsie Poopsie, something broke")
        except:
            print("Apologies, You must type in a whole number: 1, 2, or 3 (inclusive).")
            
        # Tell the user how many questions the user has answered
        print(f'Total Questions Answered: {counter}\n')

if __name__ == "__main__":
    main()    
