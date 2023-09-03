import sys
import random

#number range specified by the user from command line interface
range_start = int(sys.argv[1])
range_end = int(sys.argv[2])

#Generate the correct number from the user specified range
correct_number = random.randint(range_start,range_end)

while True:
    try:
        user_input = int(input(f'guess the right number between {range_start} and {range_end } : '))
        if 0<=user_input<11:
                if user_input == correct_number:
                    print("you are correct\nCongragulations!")
                    break
                else:
                    if user_input > correct_number:
                        print("The number is lower")
                    else:
                        print("The number is higher")
                    print("Please try again")

    except ValueError:
        # if the number entered is not within hte range or is not an int, raise exception
        print("enter a number that is valid and it is between 1-10")
        continue




