print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___/____
*******************************************************************************
''')
print("Welcome to treasure island game !!!")
print("Your mission is to find the treasure.")
print("You are standing alongside a road.Where do you want to go ?")

choice_1 = input("Left or Right ?").lower()
if choice_1 == 'left':
    print("You have reached at river side . What do you want ?")
    choice_2 = input("Swim or Wait ?? ").lower()
    if choice_2 == 'wait':
        print('''You have found a boat and crossed the river .
        You are standing outside a cave and there are three doors into it.
        Which one you will select ?''')
        choice_3 =input("Red , Yellow , Blue ?").lower()
        if choice_3 == 'red':
            print("You are burned with fire. Game over!!")
        elif choice_3 == 'yellow':
            print("Congratulations ! You have Found the treasure . You win.")
        elif choice_3 == 'blue':
            print("You are eaten by beasts . Game over !!!")
        else:
            print("Game Over !!!")
    else:
        print("You are attacked by trout . Game over !!!")
else :
    print("You have fallen into a hole . Game over !!!")
