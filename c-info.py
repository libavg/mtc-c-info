#!/usr/bin/python

from libavg import avg, anim

MoreGlueh = False
ClampActive = False

def onCursorDown(Event):
    global ClampActive

    StackNode = Player.getElementByID("stack")
    ClampNode = Player.getElementByID("clamp0")
    ClampActive = not(ClampActive)
    if ClampActive: 
        StackNode.x = ClampNode.x
        StackNode.y = ClampNode.y
        anim.fadeIn(StackNode, 100, 1)
        ClampNode.opacity = 0
    else:
        anim.fadeOut(StackNode, 100)
        ClampNode.opacity = 1

def onFrame():
    global MoreGlueh
    global ClampActive
    if not(ClampActive):
        Node = Player.getElementByID("clamp0")
#        Node.angle += 0.002
        Node.x += 0.1
        Node.y += 0.1

    Node = Player.getElementByID("gluehen")
    if MoreGlueh:
        Node.opacity += 0.002
        if Node.opacity > 0.5:
            MoreGlueh = False
    else:
        Node.opacity -= 0.002
        if Node.opacity < 0.2:
            MoreGlueh = True
    
    Node = Player.getElementByID("greece")
    Node.x -= 0.1
    Node.y -= 0.04
    for id in ["weltraum0", "weltraum1", "weltraum2", "weltraum3"]:
        Node = Player.getElementByID(id)
        Node.x -= 0.1
        Node.y -= 0.04

Player = avg.Player()
Player.loadFile('c-info.avg')
Player.setResolution(1,0,0,0)
Player.setVBlankFramerate(1)
for id in ["clamp0", "clamp1", "clamp2", "clamp3", "clamp4", "clamp5", "clamp6"]:
    Node = Player.getElementByID(id)
    Node.play()
    Node.setEventHandler(avg.CURSORDOWN, avg.TOUCH, onCursorDown)
Player.setOnFrameHandler(onFrame)
Player.addTracker()
anim.init(Player)
Player.play()
