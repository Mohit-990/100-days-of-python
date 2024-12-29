# Welcome to Python Treasure Finding game 
# Enter your first choice
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("You are standing at a roadside .")
choice1 = input("Where do you want to go Left or Right ?").lower()
if choice1 == "left":
    print("You Fall into a dig!!!!")
    print("You fail !!!")
elif choice1 == "right":
    print("You reach at a river side .")
    print("You have Either to swim and cross the river or wait for a boat .")
    print("What do you want , Swim or Wait ?")

    # Make Your second choice
    choice2 = input("Enter your choice : ").lower()
    if choice2 == "swim":
        print("You are jumping in the river.")
        print("The river is filled with crocodiles.")
        print("You are trapped in mid of river .")
        print("You lose the game !!!")
    elif choice2 == "wait":
        print("You found a boat and shift on it.")
        print('''The boat safely cross the river and you have reached in front of a cave
              it has three doors. which one you choose.''') 
         
        #Make your third choice

        choice3 = input("Choose any one door RED / Blue / Yellow .").lower() 
        if choice3 == "red":
            print("You Have select the door fiiled with fire .")
            print("You lose the game.")
        elif choice3 == "Blue":
            print("You have selected the door filled with storm .") 
            print("You lose the game !!!")   
        elif choice3 == "yellow" :
            print("You have selected the correct door .")
            print("You have found the Treasure.") 
            print("Congratulations !!! You won the game.")
        else:
            print("The door you have selected, does not exist !!")    
            print("You did not win the match !!!")
    else:
        print("Incorrect Choice ! You lose the game !!")    
else :
    print("You have selected a wrong direction !!")
    print("You lose the game .!!!!")    
    
