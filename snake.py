from turtle import Turtle


STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

MOVE_DISTANCE= 20


class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(newx, newy)

        self.segments[0].forward(MOVE_DISTANCE)



    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)

    def left(self):

        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right (self):

        if self.head.heading()!= 180:
            self.segments[0].setheading(0)


