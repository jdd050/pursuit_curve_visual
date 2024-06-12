import turtle as trtl
import numpy as np
from random import seed, randint

seed()

delay = 100 # miliseconds

# setup window
root = trtl.Screen()
root.screensize(800, 800)

# turtles
runner = trtl.Turtle(shape="triangle", visible=False)
runner.penup()
runner.color("blue")
runner.speed(2)

pursuer = trtl.Turtle(shape="triangle", visible=False)
pursuer.penup()
pursuer.color("red")
pursuer.speed(10)

# calculate quadrants
x_quadrant = (-(root.window_width()) // 2, root.window_width() // 2)
y_quadrant = (-(root.window_height()) // 2, root.window_height() // 2)

# set initial positions
runner_pos = (randint(*x_quadrant), randint(*y_quadrant))
pursuer_pos = (randint(*x_quadrant), randint(*y_quadrant))

# find a destination for the runner
x_pos = randint(*x_quadrant)
y_pos = randint(*y_quadrant)
while (abs(x_pos) > 700 or (abs(y_pos) > 700)): # prevent from going out of bounds
    x_pos = randint(*x_quadrant)
    y_pos = randint(*y_quadrant)
    
runner_end_pos = (x_pos, y_pos) 
runner.seth(runner.towards(runner_end_pos))

# place turtles and show them
pursuer.setpos(pursuer_pos)
pursuer.showturtle()
pursuer.pendown()

runner.setpos(runner_pos)
runner.showturtle()
runner.pendown()

# runner motion
def move_straight() -> None:
    runner.forward(runner.speed())
    root.ontimer(move_straight, delay)
    return None

# pursuer motion
def move_toward() -> None:
    diff_pos = np.abs(np.subtract(runner.pos(), pursuer.pos()))
    heading = pursuer.towards(runner)
    
    pursuer.seth(heading)
    print(f"HEADING: {heading} DIFF_POS: {diff_pos}")
    pursuer.forward(pursuer.speed())
    diff_pos = np.subtract(runner.pos(), pursuer.pos())
    root.ontimer(move_toward, delay)

move_straight()
move_toward()

root.mainloop()