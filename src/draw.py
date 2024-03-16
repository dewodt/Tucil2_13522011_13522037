from turtle import *
from point import Point

class Draw():
    t = Turtle()
    fullSize : bool

    def __init__(self, all_positive):
        Draw.t.screen.screensize(1600, 900)
        Draw.t.speed(8)
        self.fullSize = all_positive
        if (self.fullSize):
            Draw.t.screen.setworldcoordinates(0,0,1600,900)
        Draw.t.screen.title("Bezier Gesserit")
        Draw.t.screen.bgcolor("#000000")

    @staticmethod
    def drawDotsFromList(l : list[Point], color : str, size : int):
        Draw.t.penup()
        for i in range(len(l)):
            Draw.t.setposition(l[i].getX(), l[i].getY())
            Draw.t.dot(size, color)

    @staticmethod
    def drawLinesFromList(l : list[Point], color : str, size : int):
        Draw.t.penup()
        Draw.t.setposition(l[0].getX(), l[0].getY())
        Draw.t.pendown()
        Draw.t.pencolor(color)
        Draw.t.pensize(size)
        for i in range(1, len(l)):
            Draw.t.setposition(l[i].getX(), l[i].getY())

    @staticmethod
    def drawControlPoints(l : list[Point]):
        Draw.drawLinesFromList(l, "#FFFFFF", 5)
        Draw.drawDotsFromList(l, "#08637E", 9)

    @staticmethod
    def drawBruteForceCurve(l : list[Point]):
        Draw.drawLinesFromList(l, "#8F1D26", 7)
        Draw.drawDotsFromList(l, "#AE787E", 7) # Drive pink : "#E84298"

    @staticmethod
    def drawDNCCurve(l : list[Point]):
        Draw.drawLinesFromList(l, "#8F1D26", 7)
        Draw.drawDotsFromList(l, "#AE787E", 7) # Drive pink : "#E84298"