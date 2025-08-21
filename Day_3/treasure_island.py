treasure_island = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
"""

print(treasure_island)

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
input1 = input("Do you want to go left or right ? \n Type 'left' or 'right':\n ").lower()

if input1 == "right":
    print("You fell down in the canyon! Game over!")
else:
    print("You landed on the island surrounded by water.")
    input2 = input("Do you want to swim or wait? \n Type 'swim' or 'wait' :\n")

    if input2 == "swim":
        print("You got attacked by crocodiles! Game over!")
    else:
        print("The boat arrived and left you in front of  three doors.")
        input3 = input("Which door you want to take Red, Yellow or Blue. \n Type 'red' or 'yellow' or 'blue' : \n")
        if input3 == 'red' or input3 == 'blue':
            print("You got engulfed in flame! Game over!")
        else :
            print("You found the chest of treasure!! You win!")
