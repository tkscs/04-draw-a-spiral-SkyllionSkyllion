import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
turtle.speed(10)
for i in range (25):
    turtle.forward(20*i)
    turtle.right(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()