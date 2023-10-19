import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Turtle Racing Game")
screen.setup(width=500,height=400)
user_pick = screen.textinput(title="Make a bet",prompt="Pick a color of the turtle that will win the race").lower()
turtles = []
is_race_on = False

colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)


if user_pick:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_pick == winning_turtle:
                print(f"You won! {winning_turtle} is the winner")
            else:
                print(f"you lost.. {winning_turtle} is the winner")
        turtle_distance = random.randint(0,10)
        turtle.forward(turtle_distance)




# tim.goto(x=-230,y=180)
screen.exitonclick()

