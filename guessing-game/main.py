# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:55:10 2024

@author: anurag
Number Guessing Game
"""
# import random
import random
import time

print("WELCOME TO NUMBER GUESSING GAME\n    Made By ANURAG KUMAR")
print("use to guess number [1,2,3,4,5,6,7,8,9,0]")
print("To View the score write score\nTo quit write quit")
scoore=0
guessing_number=""
while guessing_number!="quit":
    guessing_number=input("Enter Number : ")
    # prints a random value from the list
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    comp_guess=random.choice(list1)
    print("Computer Guessing.. ")
    time.sleep(1.3)
    print("Computer Gussed ",comp_guess)
    try:

        if guessing_number=='score':
            print("Your Score is ",scoore,"\n")
        elif str(guessing_number)=="quit":
             print("Your Score is ",scoore)
             print("Thanks For Playing\n")
        elif int(guessing_number)==comp_guess:
            print("True\n")
            scoore=scoore+1
        else:
            print("Wrong \n")

        
    except:
        print("Try Again \n")
    
