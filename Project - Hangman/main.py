import random
from Stages import logo, stages
from words import word_list
import time

print(logo)
print("------------------------------------------------")
print('\n')
print("Welcome to Hangman!")
print("\n")

#Generate a random word from the list
random_word = random.choice(word_list)

display = []

word_length = len(random_word)

user_lives = 6

for i in range(word_length):
    display.append("_")

#Reduce the game difficulty by giving some clues
random_letter = random.choice(random_word)
for position in range(word_length):
    if random_word[position] == random_letter:
        display[position] = random_letter

#keep track of the user inputs to remind users if there are duplicates
user_guessed_letter = []

end_of_game = False
while not end_of_game:
    print(display)
    user_guess = input("Guess a letter:\n").lower()
    if user_guess in display:
        print(f"Letter {user_guess} already exists!")
    for position in range(word_length):
        letter = random_word[position]
        if user_guess == letter:
            display[position] = user_guess
            user_guessed_letter.append(user_guess)
    if user_guess not in random_word:
        user_lives -=1
        print(stages[user_lives])
        if user_guess in user_guessed_letter:
            print("You have already guessed that letter!")
        print(f'Letter {user_guess} is not in the word')
        print("You have lost a life")
        user_guessed_letter.append(user_guess)
        if user_lives ==0:
            print("You have lost")
            end_of_game = True
            print(f'\nThe word was {random_word}')
            break
    if "_" not in display:
        end_of_game = True
        print(f"Congratulations!\nThe word was {random_word}.\nYou have won!")
        break
time.sleep(10)




