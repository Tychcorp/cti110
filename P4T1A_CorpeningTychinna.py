# Turtle will move from step 0 in a square and loop to repeat
# Turtle will loop each square increased size of 5 each time
# Turtle will create 100 looped squares



import turtle
t = turtle.Turtle()

step =5
for x in range (100):

                 
    t.left(90)           
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.left(90)
    t.forward(step)
    t.left(90)
    t.forward(step)    

    step += 5
