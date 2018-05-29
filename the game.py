#Virtual Space game
#By Nitin

import turtle
import math
import random
import os
import time

#setup screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.tracer(3)

#Draw border
mypen=turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#create player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("classic")
player.turtlesize(3)
player.penup()
player.speed(0)

#create the score variable
score=0

#create goals
maxGoals=8
goals=[]

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("green")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))

#create enemies
maxenemies=8
enemies=[]

for ecount in range(maxenemies):
    enemies.append(turtle.Turtle())
    enemies[ecount].turtlesize(0.5)
    enemies[ecount].color("red")
    enemies[ecount].shape("circle")
    enemies[ecount].penup()
    enemies[ecount].speed(0)
    enemies[ecount].setposition(random.randint(-300,300),random.randint(-300,300))
#set speed variable
speed=1

#define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed=speed+1

def decreasespeed():
    global speed
    speed=speed-1
    
    
def isCollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    col=False
    if d<20:
        col=True
    return col

#set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor()>290 or player.xcor()<-290:
        player.right(180)
        
    #Boundary Checking
    if player.ycor()>290 or player.ycor()<-290:
        player.right(180)

    #move the goal
    for counts in range(maxGoals):
        goals[counts].forward(random.randint(0,1))
        #Boundary Checking
        if goals[counts].xcor()>290 or goals[counts].xcor()<-290:
            goals[counts].right(180)
        
        #Boundary Checking
        if goals[counts].ycor()>290 or goals[counts].ycor()<-290:
            goals[counts].right(180)
            
        #collision checking
        if isCollision(player,goals[counts]):
            goals[counts].setposition(random.randint(-290,290),random.randint(-290,290))
            goals[counts].right(random.randint(0,360))
            score=score+1
            #draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            scorestring="Score: %s"%score
            mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
    #move the enemies
    for ecounts in range(maxenemies):
        enemies[ecounts].forward(random.randint(0,1))
        #Boundary Checking
        if enemies[ecounts].xcor()>290 or enemies[ecounts].xcor()<-290:
            enemies[ecounts].right(180)
        
        #Boundary Checking
        if enemies[ecounts].ycor()>290 or enemies[ecounts].ycor()<-290:
            enemies[ecounts].right(180)
            
        #collision checking
        if isCollision(player,enemies[ecounts]):
            enemies[ecounts].setposition(random.randint(-290,290),random.randint(-290,290))
            enemies[ecounts].right(random.randint(0,360))
            score=score-1
            #draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            scorestring="Score: %s"%score
            mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

    if score==-2 or score ==10:
        break
