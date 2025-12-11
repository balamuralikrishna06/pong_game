from turtle import Turtle
MOVE=20

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)


    def go_up(self):
        new_x=self.xcor()
        new_y=self.ycor()+MOVE
        self.goto(new_x,new_y)

    def go_down(self):
        new_x=self.xcor()
        new_y=self.ycor()-MOVE
        self.goto(new_x,new_y)



