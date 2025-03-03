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
    work_completed = 0
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
            energy = energy -5
            candlelight = candlelight -5
            work_completed = work_completed +1
            hours_left = hours_left -10
        elif answer == "B":
            print()
            print("You have created half a page.")
            energy = energy -3
            candlelight = candlelight -3
            work_completed = work_completed +.5
            hours_left = hours_left - 5
        elif answer == "C":
            print()
            print("You took a short break.")
            energy = energy + 2
            candlelight = candlelight + 1
            work_completed = work_completed + 0
            hours_left = hours_left - 1
            print()
            #random chance to be blessed by the abbot when you
            #take a short break that refreshes your
            #energy and candlelight
            import random
            random_number = random.randint(0, 3)
            if random_number == 0:
                print("""You have been blessed by the abbot.
You feel rejuvenated, your candle burns brightly,
and you are able to get an extra half page done during your
break!""")
                energy = 10
                candlelight = 10
                work_completed = work_completed + .5
                hours_left = hours_left + 0

            elif random_number == 1:
                print("""You get distracted and waste 1 hour talking to brother John
in the herb garden.""")
                hours_left - 1
            else:
                print()
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
            hours_left = hours_left - 8
        elif answer == "F":
            print()
            print("You decided to check your status.")
            print()
            print("Your energy is ",energy, "out of 10")
            print("Your candlelight is ",candlelight, "out of 10")
            print("Your completed work is ",work_completed, "out of 14")
            print("Your hours left until the deadline are ",hours_left, "out of 168")
        else:
            print("Try putting in the letter of the option you want to pick!")
        if energy > 6:
            print()
            print("You feel well rested.")
        if energy <= 6 and energy > 3:
            print()
            print("You are getting tired and need to rest.")
        if energy <= 3 and energy > 0:
            print()
            print("You are in danger of passing out!")
        if energy <= 0:
            print()
            print("""You have passed out from exhaustion at work and made 
your fellow monks look bad. You are no longer allowed to help with the 
manuscript and have failed your brothers.""")
            break

        if candlelight >= 5:
            print("Your candle burns steadily.")
        if candlelight < 5 and candlelight > 2:
            print("The light from your candle grows dim.")
        if candlelight <= 2 and candlelight >= 1:
            print("Your light is dangerously low.")
        if candlelight <= 0:
            print("""Your candle has gone out and in trying to relight it, ink
has spilled over all of your hard work. You are shamed for your clumsiness
in such a pressing time. Your brothers do not allow you to continue to help
with the manuscripts as they fear you will absentmindedly destroy all of the 
manuscript pages.""")
            break

        if work_completed > 4 and work_completed < 7:
            print("You have a decent start on your work.")
        if work_completed >= 7 and work_completed <= 11:
            print("You have finished at least half of your work!")
        if work_completed > 11 and work_completed < 13:
            print("You are almost finished with your pages!")
        if work_completed >= 14 and hours_left <= 168:
            print("""You have completed your work on time and saved your scriptorium
from fading into obscurity! You and your brothers rejoice and continue the
art of manuscript making. Thank you for your diligent work and may the lord
see to it that you be reborn in paradise by the right hand of the father.""")
            break
        if hours_left <= 0 and work_completed < 14:
            print()
            print("""You have not completed your designated work in time. While the 
efforts of you and your brothers were valiant, you could not compete
with the printing press. Your beloved scriptorium struggles and eventually
is forced to close down due to lack of funds.""")
            break


main()
