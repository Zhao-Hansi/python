import turtle

# Move the Turtle to (x, y)
def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Draw a circle with radius r and color c
def circle(r, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

# Draw a rectangle with width w, height h and color c
def rectangle(w, h, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(w)
        turtle.left(90)
        turtle.fd(h)
        turtle.left(90)
    turtle.end_fill()

# Draw Peppa Pig
def peppa():
    # Face
    goto(0, -100)
    circle(100, "#F0C8B7")  # Pink
    circle(25, "#F57F71")  # Red
    goto(-20, 50)
    circle(20, "#FFFFFF")  # White
    goto(20, 50)
    circle(15, "#FFFFFF")  # White
    # Ears
    goto(-60, 110)
    circle(20, "#F0C8B7")  # Pink
    goto(60, 110)
    circle(20, "#F0C8B7")  # Pink
    # Eyes
    goto(-25, 25)
    circle(10, "#000000")  # Black
    goto(25, 25)
    circle(10, "#000000")  # Black
    # Nose
    goto(0, 10)
    circle(7, "#000000")  # Black
    # Mouth
    goto(-30, -20)
    turtle.pencolor("#000000")  # Black
    turtle.pensize(10)
    turtle.right(45)
    turtle.fd(40)
    # Body
    turtle.pensize(1)
    goto(-100, -100)
    rectangle(200, 100, "#F0C8B7")  # Pink
    # Legs
    goto(-70, -150)
    rectangle(40, 100, "#F0C8B7")  # Pink
    goto(30, -150)
    rectangle(40, 100, "#F0C8B7")  # Pink
    # Shoes
    goto(-80, -200)
    rectangle(20, 50, "#000000")  # Black
    goto(40, -200)
    rectangle(20, 50, "#000000")  # Black

peppa()

turtle.done()