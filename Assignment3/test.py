import turtle

windowsize = 1000


window = turtle.Screen()
window.setup(width = windowsize, height = windowsize)

colors = ["purple","red","orange","yellow","green"]
y_poses = [60, 30, 0, -30, -60]
opponents = []

for color, y_pos in zip(colors, y_poses):
    new_turtle = turtle.Turtle("square")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-390, y = y_pos)
    opponents.append(new_turtle)

# make turtles move

# win condition

window.exitonclick()