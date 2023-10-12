import arcade
import random

def main():
    print("Welcome to the Camel Game!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your\ndesert trek and outrun the natives.")

    miles_traveled = 0
    thrist = 0
    camel_tiredness = 0
    natives_distance = -20
    drinks_in_canteen = 6


    done = False

    while not done:

        print("A. Drink from your canteen")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the Night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What's your choice? ").upper()

        if user_choice == "Q":
            done = True
            print("You have successfully quit")
        elif user_choice == "E":
            print(f"You have traveled {miles_traveled}.")
            print(f"You have {drinks_in_canteen} in your canteen.")
            print(f"The Natives are {natives_distance} miles behind you.")
        elif user_choice == "D":
            camel_tiredness = 0
            print("Camel has Rested.")
            natives_distance += random.randrange(7,14)
            print("The natives are catching up!")
        elif user_choice == "C":
            miles = random.randrange(10,20)
            miles_traveled += miles
            print(f"You have traveled {miles} miles.")
            thrist += 1
            camel_tiredness += random.randrange(1,3)
            natives_distance += random.randrange(7,14)
            if random.randrange(20) == 5:
                print("You have found a rare oasis!")
                drinks_in_canteen = 6
        elif user_choice == "B":
            miles = random.randrange(5,12)
            miles_traveled += miles
            print(f"You have traveled {miles} miles.")
            thrist += 1
            camel_tiredness = +1
            natives_distance += random.randrange(7,14)
        elif user_choice == "A":
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                thrist = 0
        if thrist >= 6:
            print("You have died of thirst!!!")
            done = True
        if camel_tiredness >= 5:
            print("Your camel needs to rest")
        if camel_tiredness >= 8:
            print("Your camel has collapsed from dehydration")
            done = True
        if natives_distance >= miles_traveled:
            print("The natives have caught up!")
            done = True
        elif natives_distance >= 15:
            print("The natives are getting close!")
        if miles_traveled >= 200:
            print("You have made it across the desert!!!\nCONGRATULATIONS YOU BEAT THE GAME!")
        if random.randrange(20) == 5:
            print("You have found a rare oasis!")


main()