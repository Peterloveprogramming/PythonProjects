from data import data
from art import logo, vs
from replit import clear

def pick_random_object(data):
    """Randomly picks an object from the list. Returns an object"""
    random_object = choice(data)
    return random_object


def pick(objectA,objectB):
    """Prints questions onto the screen and return user's answer"""
    print(f"Compare A: {objectA['name']}, a {objectA['description']}, from {objectA['country']},has {objectA['follower_count']} million followers")
    print(vs)
    print(f"Against B: {objectB['name']}, a {objectB['description']}, from {objectB['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    return guess

def check_answer(objectA,objectB,guess):
    """Checks if user's guess is correct. Return True or False"""
    if guess == "a":
        if (objectA['follower_count'] > objectB['follower_count']):
            return True
        elif (objectA['follower_count'] == objectB['follower_count']):
            return True
        else:
            return False
    else:
        if (objectA['follower_count'] < objectB['follower_count']):
            return True
        elif (objectA['follower_count'] == objectB['follower_count']):
            return True
        else:
            return False

# Pick 2 random objects from the list
from random import choice


def higher_lower():

    Score = 0

    objectA = pick_random_object(data)

    objectB = pick_random_object(data)

    game_on = True

    while game_on:
        clear()
        print(logo)

        # user makes a guess guess
        guess = pick(objectA=objectA,objectB= objectB)

        #Checks to see if user's input is correct
        if (check_answer(objectA=objectA,objectB= objectB,guess=guess)):
            Score += 1
            print(f"{objectB['name']} has {objectB['follower_count']} million followers")
            print(f"You're right! Current score: {Score}.")
        else:
            print(f"{objectB['name']} has {objectB['follower_count']} million followers")
            print(f"Sorry, that's wrong. Final score: {Score}")
            game_on = False

        objectA = objectB
        objectB = pick_random_object(data)

higher_lower()
