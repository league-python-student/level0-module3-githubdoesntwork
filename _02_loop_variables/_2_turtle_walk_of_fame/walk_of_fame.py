import turtle

if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.color('blue', 'green')
    my_turtle.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    my_turtle.penup()
    my_turtle.setx(-300)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    for j in range (10):
        my_turtle.pendown()
        for i in range (5):
            my_turtle.forward(30)
            my_turtle.right(144)
        my_turtle.penup()
        my_turtle.forward(60)
    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
