#Rock,paper, and scissors game
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



print("Welcome to Rock,Paper and Scissors!")


rock_paper_scissors = ["rock","paper","scissors"]
rock_paper_scissors_picture = [rock,paper,scissors]

player_digit =  int(input("Please type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

player_choice = rock_paper_scissors[player_digit]

Computer_digit = random.randint(0,2)

Computer_choice = rock_paper_scissors[Computer_digit]


print(f'you have picked {player_choice}')
print(rock_paper_scissors_picture[player_digit])

print(f'Computer has picked {Computer_choice}')
print(rock_paper_scissors_picture[Computer_digit])


if player_choice == "rock":
    if Computer_choice == "rock":
        print("draw")
    elif Computer_choice =="paper":
        print("you lost")
    else:
        print("you win!")
elif player_choice == "scissors":
    if Computer_choice == "rock":
        print("you lost")
    elif Computer_choice =="paper":
        print("you win")
    else:
        print("draw")
else:
    if Computer_choice == "paper":
        print("draw")
    elif Computer_choice =="rock":
        print("you win")
    else:
        print("you lost")

