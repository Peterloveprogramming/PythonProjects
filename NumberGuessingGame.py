import sys
import random

range_start = int(sys.argv[1])
range_end = int(sys.argv[2])

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
        print("enter a number that is valid and it is between 1-10")
        continue




