from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=800, height=600)
screen.bgpic('road.gif')

user_bet = screen.textinput(title="Make Your Bet", prompt="Enter turtle's color of your choice : ")
print(user_bet)
colors = ["red", "violet", "green", "orange", "blue", "yellow", "white"]
y_positions = [-260, -172, -85, 2, 85, 172, 260]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330: # turtle has crossed the finish line
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                turtle.penup()
                turtle.goto(0, -20)
                turtle.pendown()
                turtle.hideturtle()
                turtle.write(f"You Won !! The {winning_turtle} turtle won the race", font=("Arial", 20, "bold",), align="center")
            else:
                turtle.penup()
                turtle.goto(0, -20)
                turtle.pendown()
                turtle.hideturtle()
                turtle.write(f"You Lost !! The {winning_turtle} turtle won the race", font=("Arial", 20, "bold",), align="center")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()