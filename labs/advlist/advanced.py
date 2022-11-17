#!/usr/bin/env python3
import random

def main():
    
    wordbank = ["indentation", "spaces"]
    tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 
        'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 
        'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    length=len(tlgstudents)

    # append integer 4 to the list
    wordbank.append(4)
    
    # Bonus 2
    student_number = int(input(f"Enter a student number between 1 and {length} : "))-1
    while True:
        if 0 <= student_number < length:
            break
        else:
            student_number = int(input("Try again, enter a number between 1 and {length}"))-1

    student_name = tlgstudents[student_number]
    print(f"Student is: {student_name}!")
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    # Bonus 1
    random_name = random.choice(tlgstudents)
    print(f"Random name is: {random_name}")

main()

