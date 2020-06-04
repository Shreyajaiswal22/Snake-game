 
"""
Created on Thu Jul  4 13:50:19 2019

@author: Shreya Jaiswal
"""

import turtle
import time
import random
import winsound

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake GAme")

wn.setup(width=600, height=600)
wn.tracer(0) 
wn.bgpic("background.gif")
# Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#update the score
#score +=10
#scorestring= "Score: %s" %score
pen.clear()
#pen.write(scorestring, False,align="left",font=("arial",14,"normal"))

pen.write("SCORE: 0  ", align="center", font=("Arial", 14, "italic"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        winsound.PlaySound('Basic_Rock_135.wav', winsound.SND_ASYNC)
        bulletstate="fire"
        time.sleep(1)
        head.goto(0,10)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        #update the score
#        score +=10
#        scorestring= "Score: %s" %score
#        pen.clear()
#        pen.write(scorestring, False,align="left",font=("arial",14,"normal"))
#            

        pen.write("SCORE: {} ,HIGH SCORE:{} ".format(score, high_score), align="center", font=("Arial", 24, "italic")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
       
        
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        winsound.PlaySound('.wav', winsound.SND_ASYNC)
        bulletstate="fire"
        
        

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
            #update the score
#            score +=10
#            scorestring= "Score: %s" %score
#            pen.clear()
#            pen.write(scorestring, False,align="left",font=("arial",24,"normal"))
#            pen.write("HIGH SCORE :{}".format(high_score),align="right", font=("arial",24,"normal"))
#            

        
            pen.clear()
            pen.write("SCORE: {} , HIGH SCORE:{}".format(score, high_score), align="center", font=("Arial", 24, "italic")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,10)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            #update the score
#             pen.clear()
#            pen.write(scorestring, False,align="left",font=("arial",14,"normal"))
#            pen.write("HIGH SCORE :{}".format(high_score),align="right", font=("arial",24,"normal"))
#            d = turtle.Turtle()
#            print("GAME OVER")
           
#            d.write("GAME OVER\n" + scorestring, align="center", font=("Arial", 35, "bold"))

            pen.clear()
            pen.write("SCORE: {}, HIGH SCORE:{}".format(score, high_score), align="center", font=("Arial", 24, "italic"))

    time.sleep(delay)

wn.mainloop()