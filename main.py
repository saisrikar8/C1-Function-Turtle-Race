'''
04/01/2021

Python Function
- Bundles a set of code that you want to use repeatedly

Define a function
1)
def FUNCTIONNAME():
  BODY

2)
def FUNCTIONNAME(PAREMETER)
  BODY w/PARAMETER



def drawSquare():
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)

def drawSqaure2(l):
  pen.color("red")
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)
  pen.fd(l)
  pen.left(90)

drawSquare()
drawSqaure2(150)

circle(radius, angle/degrees, step/sides)

import turtle
import random

#set up a turtle/pen
pen = turtle.Turtle()

def drawShapes(radius, side):
  pen.circle(radius, 360, side)

#drawShapes(100, 3)
#drawShapes(100, 6)

for i in range(20):
  pen.speed(1000000)
  pen.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  drawShapes(100, 3 + i)
'''

import turtle
import random

# Start out with showing the game
# Setup turtle to draw

p1 = turtle.Turtle()
p1.color("spring green")

x = -140
y = 140

p1.penup()
p1.goto(x, y)
p1.right(90)
p1.speed(100)

for i in range(16):
  p1.pendown()
  p1.write(i)
  p1.penup()

  p1.penup()
  p1.fd(10)

  p1.pendown()
  p1.fd(200)

  p1.penup()
  p1.goto(x + 20 * (i + 1),140)


# turtle1
p1.speed(3)
p1.color(random.randint(0,255), random.randint(0,255), random.randint(0, 255))
p1.penup()
p1.left(90)
p1.goto(-155, 100)
p1.pendown()
p1.shape("turtle")
p1.speed(100)
# turtle2 (-155, 70)
p2 = turtle.Turtle()
p2.speed(3)
p2.color(random.randint(0,255), random.randint(0,255), random.randint(0, 255))
p2.penup()
p2.goto(-155, 70)
p2.pendown()
p2.shape("turtle")
p2.speed(100)
# turtle3 (-155,40)
p3 = turtle.Turtle()
p3.speed(3)
p3.color(random.randint(0,255), random.randint(0,255), random.randint(0, 255))
p3.penup()
p3.goto(-155, 40)
p3.pendown()
p3.shape("turtle")
p3.speed(100)
# turtle4 (-155, 10)
p4 = turtle.Turtle()
p4.speed(3)
p4.color(random.randint(0,255), random.randint(0,255), random.randint(0, 255))
p4.penup()
p4.goto(-155, 10)
p4.pendown()
p4.shape("turtle")
p4.speed(100)
for t in range(105):
  p1.fd(random.randint(1,5))
  p2.fd(random.randint(1,5))
  p3.fd(random.randint(1,5))
  p4.fd(random.randint(1,5))

