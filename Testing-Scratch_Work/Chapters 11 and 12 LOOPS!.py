#for loop

"""Repeat number in range parameter"""
#for i in range(5):
    #print("I will not chew gum in class.")

"""Repeat for input of repetitions"""
#repetitions = int(input("How many times should I repeat? "))

"""Loop that many times"""
#for i in range(repetitions):
    #print("I will not chew gum in class.")

"""Using i variable"""
#counting lists, computers start counting at zero
#it stops before the parameter value
#for i in range(10):
    #print(i)

"""you can also add the number to i in the print parameter"""

"""Count by 2s to 10"""
#for i in range(2, 12, 2):
    #print(i)

"""backward counting"""
#for i in range(10, 0, -1):
    #print(i)

"""Running total"""
#total = 0
#for i in range(5):
    #new_number = int(input("Enter a number: " ))
    #total = total + new_number
#print("The total is: ", total)

"""WHILE loops"""
#while True: # Loop forever
    #quit = input("Do you want to quit? ")
   # if quit == "y":
        #break

    #attack = input("Does your elf attack the dragon? ")
   # if attack == "y":
     #   print("Bad choice, you died.")
       # break

    #attack = input("Does your elf attempt to steal the gold? ")
    #if attack == "y":
       # print("Bad choice, you died.")
        #break

"""Random number chance"""
import random


# The line below will "roll the dice" 20 times.
# Don't copy this 'for' loop into your program.
# It is just here so we can try this example over and over.
#for i in range(20):

    # The line below will roll a random number 0-4.
    # If we roll a '0' then print that we encountered a dragon.
    #if random.randrange(5) == 0:
        #print("DRAGON!!!")
    #else:
        #print("No dragon.")

"""
Random Number Guessing Game
"""
import random


def main():

    print("Hi! I'm thinking of a random number between 1 and 100.")

    # NEW CONCEPT
    # Create a secret number
    secret_number = random.randrange(1, 101)

    # Initialize our attempt count, we start with attempt 1.
    user_attempt_number = 1

    # Set user guess to something secret number can't be, so we can
    # get our 'while' loop started.
    user_guess = 0

    # NEW CONCEPT
    # Loop until user_guess our secret number, or we run out of attempts.
    while user_guess != secret_number and user_attempt_number < 8:

        # Tell the user what attempt we are on, and get their guess:
        print("--- Attempt", user_attempt_number)
        user_input_text = input("Guess what number I am thinking of: ")
        user_guess = int(user_input_text)

        # Print if we are too high or low, or we got it.
        if user_guess > secret_number:
            print("Too high.")
        elif user_guess < secret_number:
            print("Too low.")
        else:
            print("You got it!")

        # Add to the attempt count
        user_attempt_number += 1

    # Here, check to see if the user didn't guess the answer, and ran out of tries.
    # Let her know what the number was, so she doesn't spend the rest of her life
    # wondering.
    if user_guess != secret_number:
        print("Aw, you ran out of tries. The number was " + str(secret_number) + ".")

# Call the main function
main()