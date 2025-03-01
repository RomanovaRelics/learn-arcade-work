def main():
    print()
    print("Welcome to The Scriptorium!")
    print()
    print("""It is the year of our lord 1465. You are a Benedictine monk 
working in a German abbey's scriptorium. Pressure has been building on your
abbey to modernise and use the widely commercialized printing press instead 
of transcribing books by hand. In order to prove you are not obsolete, each of 
your fellow monks must produce 14 manuscript pages in a week. Can you manage to 
ward off sleep and darkness to save your scriptorium?""")
    # boolean variable
    done = False

    #set variables
    energy = 10
    candlelight = 10
    work_completed = 14
    hours_left = 168 #7 days, 24 hours a day, 168 total hours to finish

    # loop while done = false
    while not done:
        print()
        print("What are you going to do?")
        print()
        print("A. Create one page")
        print("B. Create half page")
        print("C. Take a short break")
        print("D. Light new candle")
        print("E. Stop for the day")
        print("F. Status Check")
        print("Q. Quit")
        print()
        answer = input("What is your choice? ")
        answer = answer.upper()
        if answer == "Q":
            done = True
            print()
            print("You have quit.")
        elif answer == "A":
            print()
            print("You have created one page.")
            energy = energy -6
            candlelight = candlelight -6
            work_completed = work_completed -1
            hours_left = hours_left -10
        elif answer == "B":
            print()
            print("You have created half a page.")
            energy = energy -3
            candlelight = candlelight -3
            work_completed = work_completed -.5
            hours_left = hours_left - 5
        elif answer == "C":
            print()
            print("You took a short break.")
            energy = energy + 2
            candlelight = candlelight + 1
            work_completed = work_completed + 0
            hours_left = hours_left - 1
        elif answer == "D":
            print()
            print("You lit a new candle.")
            energy = energy - 1
            candlelight = 10
            work_completed = work_completed + 0
            hours_left = hours_left - .5
        elif answer == "E":
            print()
            print("You have stopped to sleep.")
            energy = 10
            candlelight = 10
            work_completed = work_completed + 0
            hours_left = hours_left - 7
        elif answer == "F":
            print()
            print("You decided to check your status.")
            print()
            print("Your energy is ",energy, "out of 10")
            print("Your candlelight is ",candlelight, "out of 10")
            print("Your completed work is ",work_completed, "out of 14")
            print("Your hours left until the deadline are ",hours_left, "out of 168")




main()
