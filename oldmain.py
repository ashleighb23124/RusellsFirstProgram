import turtle

turtle.setup (600,600)
turtle.bgcolor("blue")
turtle.pencolor("pink")

turtle.pensize(6)
turtle.speed(13)

def innerSquare():   #defined the filter
  size=1
  for count in range(98):
    turtle.forward(size)
    turtle.right(90)
    size+=1

innerSquare()  #calling the function

def circle():
  for count in range(36):
    turtle.forward(20)
    turtle.right(10)


def outerSquare():
  turtle.pencolor("yellow")
  turtle.pensize(2)
  for count in range (4)
    turtle.forward(50)
    turtle.right(90)

innerSquare()   #calling the function
turtle.goto(0,0)
for count in range(200)
  outerSquare()
  turtle.right(10)