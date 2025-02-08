# Abduljabbar Said
# March 2019
from graphics import Point, GraphWin, Rectangle, Circle, Line, Polygon, Text

def main():
    
    win = GraphWin ("Blue's Clues House", 750, 750)
    top = Rectangle(Point(750, 375), Point(0, 0))
    top.setFill("Deep Sky Blue")
    top.setOutline("Deep Sky Blue")
    top.setWidth(2)
    top.draw(win)

    bot = Rectangle(Point(750, 750), Point(0, 375))
    bot.setFill("Green")
    bot.setOutline("Green")
    bot.setWidth(2)
    bot.draw(win)

    mid = Rectangle(Point(300, 750), Point(450, 375))
    mid.setFill("Grey")
    mid.setOutline("Grey")
    mid.setWidth(2)
    mid.draw(win)

    c1 = Circle(Point(100, 200), 50)
    c1.setFill("White")
    c1.setOutline("white")
    c1.setWidth(1)
    c1.draw(win)

    c2 = Circle(Point(155, 145), 50)
    c2.setFill("White")
    c2.setOutline("white")
    c2.setWidth(1)
    c2.draw(win)

    c3 = Circle(Point(190, 200), 50)
    c3.setFill("White")
    c3.setOutline("white")
    c3.setWidth(1)
    c3.draw(win)

    c4 = Circle(Point(230, 145), 50)
    c4.setFill("White")
    c4.setOutline("white")
    c4.setWidth(1)
    c4.draw(win)

    c5 = Circle(Point(480, 200), 50)
    c5.setFill("White")
    c5.setOutline("white")
    c5.setWidth(1)
    c5.draw(win)

    c6 = Circle(Point(535, 145), 50)
    c6.setFill("White")
    c6.setOutline("white")
    c6.setWidth(1)
    c6.draw(win)

    c7 = Circle(Point(570, 200), 50)
    c7.setFill("White")
    c7.setOutline("white")
    c7.setWidth(1)
    c7.draw(win)

    c8 = Circle(Point(610, 145), 50)
    c8.setFill("White")
    c8.setOutline("white")
    c8.setWidth(1)
    c8.draw(win)

    trunk = Rectangle(Point(630, 375), Point(670, 280))
    trunk.setFill("Brown")
    trunk.setOutline("Brown")
    trunk.setWidth(1)
    trunk.draw(win)

    trunk1 = Rectangle(Point(600, 295), Point(630, 285))
    trunk1.setFill("Brown")
    trunk1.setOutline("Brown")
    trunk1.setWidth(1)
    trunk1.draw(win)

    tire = Circle(Point(605, 335), 20)
    tire.setFill("Black")
    tire.setOutline("Black")
    tire.setWidth(1)
    tire.draw(win)

    tire1 = Circle(Point(605, 335), 10)
    tire1.setFill("Deep Sky Blue")
    tire1.setOutline("Black")
    tire1.setWidth(1)
    tire1.draw(win)

    rope = Line(Point(605, 284), Point(605, 325))
    rope.setFill("Grey")
    rope.setOutline("Grey")
    rope.setWidth(2)
    rope.draw(win)

    leaf = Circle(Point(650, 215), 70)
    leaf.setFill("Lime Green")
    leaf.setOutline("Lime Green")
    leaf.setWidth(2)
    leaf.draw(win)

    ap1 = Circle(Point(620, 215), 10)
    ap1.setFill("Red")
    ap1.setOutline("Dark Red")
    ap1.setWidth(1)
    ap1.draw(win)

    ap2 = Circle(Point(670, 245), 10)
    ap2.setFill("Red")
    ap2.setOutline("Dark Red")
    ap2.setWidth(1)
    ap2.draw(win)

    ap3 = Circle(Point(675, 185), 10)
    ap3.setFill("Red")
    ap3.setOutline("Dark Red")
    ap3.setWidth(1)
    ap3.draw(win)

    pole = Rectangle(Point(640, 675), Point(655, 580))
    pole.setFill("Dark Magenta")
    pole.setOutline("Dark Magenta")
    pole.setWidth(1)
    pole.draw(win)

    box = Rectangle(Point(715, 510), Point(565, 580))
    box.setFill("Medium Purple")
    box.setOutline("Medium Purple")
    box.setWidth(1)
    box.draw(win)

    face = Rectangle(Point(610, 510), Point(565, 580))
    face.setFill("Plum")
    face.setOutline("Plum")
    face.setWidth(1)
    face.draw(win)

    sm1 = Line(Point(570, 555), Point(570, 575))
    sm1.setFill("Fuchsia")
    sm1.setOutline("Fuchsia")
    sm1.setWidth(3)
    sm1.draw(win)

    sm2 = Line(Point(605, 555), Point(605, 575))
    sm2.setFill("Fuchsia")
    sm2.setOutline("Fuchsia")
    sm2.setWidth(3)
    sm2.draw(win)

    sm2 = Line(Point(570, 574), Point(605, 574))
    sm2.setFill("Fuchsia")
    sm2.setOutline("Fuchsia")
    sm2.setWidth(4)
    sm2.draw(win)
    
    mt = Rectangle(Point(583, 505), Point(593, 515))
    mt.setFill("Grey")
    mt.setOutline("Grey")
    mt.setWidth(1)
    mt.draw(win)

    eye1 = Circle(Point(576, 533), 11)
    eye1.setFill("White")
    eye1.setOutline("Black")
    eye1.setWidth(1)
    eye1.draw(win)

    ppl1 = Circle(Point(576, 533), 7)
    ppl1.setFill("Black")
    ppl1.setOutline("White")
    ppl1.setWidth(1)
    ppl1.draw(win)
    
    eye2 = Circle(Point(596, 533), 11)
    eye2.setFill("White")
    eye2.setOutline("Black")
    eye2.setWidth(1)
    eye2.draw(win)

    ppl2 = Circle(Point(596, 533), 7)
    ppl2.setFill("Black")
    ppl2.setOutline("White")
    ppl2.setWidth(1)
    ppl2.draw(win)

    arm = Rectangle(Point(640, 545), Point(660, 450))
    arm.setFill("Fuchsia")
    arm.setOutline("Fuchsia")
    arm.setWidth(1)
    arm.draw(win)

    hand = Rectangle(Point(640, 445), Point(695, 485))
    hand.setFill("Fuchsia")
    hand.setOutline("Fuchsia")
    hand.setWidth(1)
    hand.draw(win)
    
    wt = Text(Point(100, 25), "WELCOME TO")
    wt.setFill("Blue")
    wt.draw(win)

    bc = Text(Point(100, 40), "BLUE'S CLUE'S")
    bc.setFill("Blue")
    bc.draw(win)

    insert = Text(Point(375, 335), "The House Should Be Here")
    insert.draw(win)

    made = Text(Point(100, 700), "MADE BY")
    made.setFill("Lime Green")
    made.draw(win)
    
    dulio = Text(Point(100, 715), "ABDULJABBAR SAID")
    dulio.setFill("Lime Green")
    dulio.draw(win)
    
    click1 = win.getMouse()
    click2 = win.getMouse()

    house = Rectangle(click1, click2)
    house.setFill("Yellow")
    house.setOutline("Orange")
    house.setWidth(2)
    house.draw(win)

    click3 = win.getMouse()
    width = abs ((click1.getX())-(click2.getY()))
    y = click3.getY()
    x = click3.getX()

    yBottom = click1.getY()
    wod =  width*0.85

    wow1 = wod*0.65
    wow2 = wod*0.65

    p1 = Point(x - width * 0.60, yBottom)
    p2 = Point(x + width * 0.40, y)

    door = Rectangle(p1, p2)
    door.setFill("Purple")
    door.setOutline("Black")
    door.setWidth(2)
    door.draw(win)

    click4 = win.getMouse()
    y2 = click4.getY()
    x2 = click4.getX()

    p3 = Point(x2 - ((wow1)/2), y2 - ((wow1)/2))
    p4 = Point(x2 + ((wow1)/2), y2 + ((wow1)/2))

    window1 = Rectangle(p3, p4)
    window1.setFill("Indian Red")
    window1.setOutline("Red")
    window1.draw(win)

    click5 = win.getMouse()
    y3 = click5.getY()
    x3 = click5.getX()

    p5 = Point(x3 - ((wow2)/2), y3 - ((wow2)/2))
    p6 = Point(x3 + ((wow2)/2), y3 + ((wow2)/2))

    window2 = Rectangle(p5, p6)
    window2.setFill("Indian Red")
    window2.setOutline("Red")
    window2.draw(win)

    click6 = win.getMouse()
    p7 = Point(click1.getX(), click2.getY())
    roof = Polygon(click6, p7, click2)
    roof.setFill("Red")
    roof.setOutline("Dark Red")
    roof.setWidth(2)
    roof.draw(win)

main()
