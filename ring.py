#Day 1: Ring
import turtle
wn = turtle.Screen()
wn.bgcolor('grey')
Ring = turtle.Turtle()
Ring.speed(0)
Ring.pensize(1)
Ring.color('black')
def drawCircle(t,size):
    for i in range(15):
        t.circle(size)
        size=size-5
def draw(t,size,repeat):
  for i in range (repeat):
  	drawCircle(t,size)
  	t.right(360/repeat)
draw(Ring,100,8)
