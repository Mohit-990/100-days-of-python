import random

from Hangman_words import word_list
from hangman_art import Stages,logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print("word to guess : " + placeholder)

game_over = False
correct_guesses = []

while not game_over:

    print(f"**************** {lives}/6 LIVES LEFT ****************")
    guess = input("Guess a letter : ").lower()

    if guess in correct_guesses:
        print(f"You already guessed {guess}.")
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"********************** IT was {chosen_word} You Lose ! **********************")

    if "_" not in display:
        print("You Win !")
        game_over = True
        print("********************** You Win ! **********************")

    print(Stages[lives])
