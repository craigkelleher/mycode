#!/usr/bin/env python3
counter = 0
answer = " "

# Test if brian or shubbery was the given input
while counter < 3 and (answer != "brian" and answer != "shrubbery"):
    #increment counter by 1
    counter += 1
    # Prompt the user for input
    print('Finish the movie title within 3 turns, "Monty Python\'s The Life of _i_____"')
    # store input as answer, and capitalize input
    answer = input("Your guess--> ").lower()
    # check user input against secret
    if answer == 'brian':
        print('Correct')
        break
    elif answer == "shubbery":
        print("You gave the super secret answer!")
    # break if user used up 3 tries
    elif counter == 3:
        print("Sorry, the answer was Brian.")
        break
    # if user input did not match either secret answer
    else:
        print("Sorry! Try again!")

