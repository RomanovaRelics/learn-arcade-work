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
for i in range(10,0,-1):
    for j in range(i):
        print(j, end=" ")
    print()