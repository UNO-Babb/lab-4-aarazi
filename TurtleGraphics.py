import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, size, sides):
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(360/sides)
        
def fillCorner (myTurtle, size, sides, corner):
    drawPolygon(myTurtle, size, sides)
    if corner==2:
        myTurtle.forward(size/2)
    elif corner==3:
        myTurtle.forward(size)
        myTurtle.right(360/corner)
        myTurtle.forward(size/2)
    elif corner==4:
        myTurtle.forward(size)
        myTurtle.right(360/corner)
        myTurtle.forward(size/2)
        
    myTurtle.begin_fill()
    drawPolygon(myTurtle,(size/2),sides)
    myTurtle.end_fill()    
    
def squaresInSquares (myTurtle, num):
    size=10
    for i in range (num):
        drawPolygon(myTurtle, size, 4)
        size = size+5
        myTurtle.penup()
        myTurtle.left (90)
        myTurtle.forward(size/5)
        myTurtle.left (90)
        myTurtle.forward(size/5)
        myTurtle.right(180)
        myTurtle.pendown()

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 50, 5) #draws a pentagon
    #drawPolygon(myTurtle, 50, 8) #draws an octogon
    #drawPolygon(myTurtle,50,4)
    
    #fillCorner (myTurtle, 50, 4, 4)
    
    squaresInSquares (myTurtle,3)
    

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
