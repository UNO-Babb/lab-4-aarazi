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
        myTurtle.right(360/sides)
        myTurtle.forward(size)
        myTurtle.right(360/sides)
        myTurtle.forward(size/2)
    elif corner==4:
        myTurtle.forward(size)
        myTurtle.right(360/sides)
        myTurtle.forward(size/2)
        
    myTurtle.begin_fill()
    drawPolygon(myTurtle,(size/2),sides)
    myTurtle.end_fill()    
    
def squaresInSquares (myTurtle, num, size, increase):
    for i in range (num):
        drawPolygon(myTurtle, size, 4)
        size = size+increase
        myTurtle.penup()
        myTurtle.left (90)
        myTurtle.forward(increase/2)
        myTurtle.left (90)
        myTurtle.forward(increase/2)
        myTurtle.right(180)
        myTurtle.pendown()

def main():
    myTurtle = turtle.Turtle()
    drawPolygon(myTurtle,50,4) #draws a square
    drawPolygon(myTurtle, 50, 5) #draws a pentagon
    drawPolygon(myTurtle, 50, 8) #draws an octogon

    myTurtle.penup()
    myTurtle.goto(150,150)
    myTurtle.pendown()
    
    fillCorner (myTurtle, 50, 4, 2) #draws a square with top right corner filled in
    
    myTurtle.penup()
    myTurtle.goto(-150,150)
    myTurtle.pendown()
    
    fillCorner (myTurtle, 50, 4, 3)  #draws a square bottom left corner filled in
    
    myTurtle.penup()
    myTurtle.goto(-150,-150)
    myTurtle.pendown()
    
    squaresInSquares (myTurtle,5,12,6)#draws 5 concentric squares
    
    myTurtle.penup()
    myTurtle.goto(150,-150)
    myTurtle.pendown()
    
    squaresInSquares (myTurtle,3,12,10)#draws 3 concentric squares
    

main()
