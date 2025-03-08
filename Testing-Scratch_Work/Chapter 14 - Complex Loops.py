"""print ********** using for loop"""
#for i in range(10):
    #print("*", end= " ")

"""Print first line 10*, second 5*, third 20*"""
#for i in range(10):
    #print("*", end= " ")
#print()
#for i in range(5):
    #print("*", end= " ")
#print()
#for i in range(20):
    #print("*", end= " ")
#print()

"""full square of 10 by 10*, nested loop"""
# i = rows, j = columns
#for i in range(10):
    #for j in range(10):
        #print("*", end= " ")
    #print()

"""full rectangle 5* by 10*"""
#i = rows, j = columns
#for i in range(10):
    #for j in range(5):
        #print("*", end= " ")
    #print()

"""printing 10 by 10 square of 0-9"""
#for i in range(10):
    #for j in range(10):
        #j is where you add changes
        #print(j, end=" ")
    #print()

"""triangle with increasing numbers from 0 to 0-9 at the bottom by row"""
#for i in range(11):
    #for j in range(i):
        #print(j, end=" ")
    #print()

"""Problem 9"""
#for row in range(10):
    #for j in range(row):
        #print(" ", end=" ")
    #for j in range(10 - row):
        #print(j, end=" ")
    #print()

"""Problem 10"""
#for i in range(1, 10):
    #for j in range(1, 10):
        # Extra space?
        #if i * j < 10:
            #print(" ", end="")
        #print(i * j, end=" ")
    # Move down to the next row
    #print()

"""Problem 11"""
#for i in range(10):
    # Print leading spaces
    #for j in range(10 - i):
        #print (" ", end=" ")
    # Count up
    #for j in range(1, i + 1):
        #print (j, end=" ")
    # Count down
    #for j in range(i - 1, 0, -1):
        #print (j, end=" ")
    # Next row
    #print()

"""Problem 12"""
#for i in range(10):
     #Print leading spaces
    #for j in range(9 - i):
        #print(" ", end=" ")
    # Count up
    #for j in range(1, i + 1):
        #print(j, end=" ")
    # Count down
    #for j in range(i - 1, 0, -1):
        #print(j, end=" ")
    # Next row
    #print()

#for i in range(10):
    # Print leading spaces
    #for j in range(i + 1):
        #print(" ", end=" ")
    # Count down
    #for j in range(1, 9 - i):
        #print(j, end=" ")
    # Next row
    #print()

"""Problem 13"""
for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i + 2):
        print(" ", end=" ")
    # Count up
    for j in range(1, 9 - i):
        print(j, end=" ")
     #Count down
    for j in range(7 - i, 0, -1):
        print(j, end=" ")
    print()