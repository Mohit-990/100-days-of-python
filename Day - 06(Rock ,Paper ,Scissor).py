import random
def game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    # Paper
    paper = '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    '''

    # Scissors
    scissor = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    game_images = [rock, paper, scissor]
    user_choice = int(input("What do you choose ? Type 0 for Rock , 1 for Paper and 2 for Scissor : "))
    if 0 <= user_choice <= 2:
        print(f"Your Choice {user_choice}")
        print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"computer choice {computer_choice}")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("Invalid Choice ! You Lose !")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win !")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer Win !")
    elif computer_choice > user_choice:
        print("Computer wins !")
    elif user_choice > computer_choice:
        print("You Win !")
    elif computer_choice == user_choice:
        print("It's a draw !")
play_again = "y"
while play_again.lower() == "y":
    game()
    play_again = input("Do you want to play again? Type 'y' for Yes or any other key to quit : ")
print("Thanks for Playing !")

