from main import *
from graphics import *

'''
|--------------------------------------------------------------------|
|Names: Pavel Trninkov, Alex Bachynsky                               |
|Programming Project: Milestone #1                                   |
|--------------------------------------------------------------------|
'''

def game():
    window = GraphWin("Hanoi Towers", 800, 600)
    while window.isOpen():
        quit = button(Point(700, 25), Point(750, 50), "Quit", window)
        save = button(Point(700, 75), Point(750, 100), "Save", window)
        load = button(Point(700, 125), Point(750, 150), "Load", window)
        mouse = window.getMouse()
        if quit[0] <= mouse.getX() <= quit[1] and quit[2] <= mouse.getY() <= quit[3]:
            window.close()
        if save[0] <= mouse.getX() <= save[1] and save[2] <= mouse.getY() <= save[3]:
            save_game({})
        if load[0] <= mouse.getX() <= load[1] and load[2] <= mouse.getY() <= load[3]:
            load_game()

def button(p1:Point, p2:Point, text:str, window:GraphWin) -> list:
    button = Rectangle(p1, p2)
    button_text = Text(button.getCenter(), text)
    button.setFill(color_rgb(100, 100, 100))
    button_text.setFill(color_rgb(0,0,0))
    button_text.setSize(14)
    button.draw(window)
    button_text.draw(window)
    return [button.getP1().getX(), button.getP2().getX(), button.getP1().getY(), button.getP2().getY()]
    

game()