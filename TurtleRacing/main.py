from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=1000, height=370)
bet = screen.textinput(title='Make your bet',
                       prompt='Which Turtle will win the race? Chose a color: ')


lst = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
speed = [5, 10, 15, 20, 25]
turtles = []
y = -90

for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(lst[i])
    new_turtle.goto(-470, y)
    y += 30
    turtles.append(new_turtle)

if bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 465:
            race_is_on = False
            win_color = turtle.pencolor()
            if win_color == bet.lower():
                print(
                    f'Winner is {win_color} turtle!, you win!\nClick to exit')
            else:
                print(
                    f'Winner is {win_color} turtle!, you lose!\nClick to exit')
        rand_speed = random.choice(speed)
        turtle.forward(rand_speed)

screen.exitonclick()
