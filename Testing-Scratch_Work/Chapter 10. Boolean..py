"""Boolean data type"""
from Tools.scripts.mailerdaemon import emparse_list_from

#a = True
#c = "True"

#if a == c:
    #print("A and c are equal.")
#else:
    #print("This is false")


#How to use the not function.
#a = False
#if not a:
   # print("A is false.")

#Any number other than zero negative or positive or floats and integers are True.
#Zero is always false

#Testing boolean values
#a = True
#b = False

#if a and b:
    #print("coolness")

#INTERACTIVE with chained function or int can be seperate
#get input from user and convert to integer
#temperature = int(input("What is the temperature in F?"))

#Do our comparison this is BOOLEAN TOO! The answer is true or false.
#ifs elifs and elses are conditions that determine how the code block beneath it
#Top value first. Evaluates top down.
#if temperature > 110:
    #print("You could fry eggs on the pavement!")
#elif temperature > 90:
    #print("It is hot outside!")
#elif temperature < 30:
    #print("It is cold outside!")
#else:
    #print("It is not hot outside.")

#print("Done!")

#With text - string objects
user_name = input("What is your name? ")

#.lower makes the input answer all lowercase .upper all uppercase
if user_name.lower() == "makenzie" or user_name.lower() == "mary":
    print("You have an awesomesauce name!")
else:
    print("Eh...")
