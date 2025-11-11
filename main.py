from random import Random
import time
from mapGenerator import GameMap, CaveMap
from randomNameGenerator import RandomNameGenerator
import os
import sys
import keyboard
from windowsConsoleGraphics import GameWindow


def cls(n = 0):
    if n == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('\b'*n)

def initializeGameWindowDict():
    # Create Game Window Dictionary
    gameWindowDict = {}
    for j in range(0, consoleHeight):
        for i in range(0, consoleWidth):
            indexString = str(i) + "," + str(j)
            gameWindowDict[indexString] = "*"
    return gameWindowDict

def drawGameWindowBorders():
    pass

def returnFrameStringFromDict(dictionaryToConvert):
    frameString = ""
    for j in range(0, consoleHeight):
        for i in range(0, consoleWidth):
            indexString = str(i) + "," + str(j)
            frameString += dictionaryToConvert[indexString]
        if j < consoleHeight - 1:
            frameString += str("\n")
    frameString += str("\033[H\033[3J")
    return frameString

def flagConsoleResize(consoleWidth,consoleHeight):
    # Clear the screen in the case of a screen resize so redrawing frames works
    ResizedFlag = False
    testvar = os.get_terminal_size().lines - HeightOffset
    if consoleHeight != testvar:
        return True
    testvar = os.get_terminal_size().columns - WidthOffset
    if consoleWidth != testvar:
        return True
    return False

def drawStringToDict(dict,string,x,y):
    indexString = ""
    for i in range(len(string)):
        indexString = str(x+i) + "," + str(y)
        screenBuffer[indexString] = string[i]
    return dict

def drawStringToDictExt(dict,string,x,y,alignH,alighV,wrapFlag):
    pass

def getLatencyString():
    pass


if __name__ == '__main__':
    #Fixes Screen Flickering:
    os.system("")

    print(sys.path)
    print(os.getcwd())
    timeKepper = time.time()
    rand = Random()
    seed = rand.randint(0, 100000)
    width = 280
    height = 68
    openNess = .55
    smoothStep = 5
    minRoomSize = 10
    entryPoints = []
    exitPoints = []

    entryPoints = [
                    [rand.randint(1, width - 2), 0],
    #                [rand.randint(1, width - 2), height - 1],
    #                [width - 1, rand.randint(1, height - 2)],
    #                [0, rand.randint(1, height - 2)]
                    ]
    exitPoints = [
    #                [rand.randint(1, width - 2), 0],
                    [rand.randint(1, width - 2), height - 1],
    #                [width - 1, rand.randint(1, height - 2)],
    #                [0, rand.randint(1, height - 2)]
                    ]

    #Map Creation
    a = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    a.generateMap()
    a.printMap(a.getMap())
    fillMap = a.generateFillMap()
    a.printMapValues(fillMap)
    print(a)
    print(a.entryPoints[0])
    print(a.exitPoints[0])


    #GameProperties
    exitFlag =False
    starttime = time.time()
    fps = 0
    fpsflag = 0
    HeightOffset = 0
    WidthOffset = 0
    consoleHeight = os.get_terminal_size().lines-HeightOffset
    consoleWidth = os.get_terminal_size().columns-WidthOffset
    consoleManager = GameWindow()
    playerx = 0
    playery = 0
    movementTimer = time.time()
    movementflag = .2
    lagTest = time.time()




    #Old Screen Clearing Code:
    #os.system('cls')
    #print("\033[H\033[3J", end="")

    #Slowly Clear the Screen first so hack for redrawing frames works
    cls()

    screenBuffer = initializeGameWindowDict()

    #PRIMARY GAME LOOP
    while (exitFlag == False):

        #Flag Console Resize
        if (flagConsoleResize(consoleWidth,consoleHeight)):
            testvar = os.get_terminal_size().lines - HeightOffset
            if consoleHeight != testvar:
                consoleHeight = testvar
                cls()
            testvar = consoleWidth = os.get_terminal_size().columns - WidthOffset
            if consoleWidth != testvar:
                consoleWidth = testvar
                cls()
            screenBuffer = initializeGameWindowDict()


        #Input Handling
        try:
            if keyboard.is_pressed('Esc'):
                print("\nyou pressed Esc, so exiting...")
                exitFlag = True
                #sys.exit(0)
            if keyboard.is_pressed('d'):
                if time.time() > movementTimer+movementflag:
                    playerx += 1
                    movementTimer = time.time()
            if keyboard.is_pressed('a'):
                if time.time() > movementTimer+movementflag:
                    playerx -= 1
                    movementTimer = time.time()
            if keyboard.is_pressed('w'):
                if time.time() > movementTimer+movementflag:
                    playery -= 1
                    movementTimer = time.time()
            if keyboard.is_pressed('s'):
                if time.time() > movementTimer+movementflag:
                    playery += 1
                    movementTimer = time.time()
        except:
            break


        #Handling Calculating and Drawing FPS
        if time.time() < starttime + 1:
            fpsflag += 1
        else:
            fps = fpsflag
            fpsflag = 0
            starttime = time.time()
        fpsString = "FPS:"+str(fps) + " " + str(consoleWidth) +"x" + str(consoleHeight)
        drawStringToDict(screenBuffer,fpsString,1,consoleHeight-1)


        #Print Screen Buffer to Console
        sys.stdout.write(returnFrameStringFromDict(screenBuffer))


    # Old Code to Draw My Cave Maps
    # drawnStringForConsole = a.returnMapStringCharacters(a.getMap())
    # print(drawnStringForConsole)

    # r = RandomNameGenerator()
    # for i in range(1):
    #     print(r.returnRandomFirstName("i"))
    # for i in range(1):
    #     print(r.returnRandomLastName())
    # for i in range(10):
    #     print(r.returnRandomFullName("i"))
    # lastName = r.returnRandomLastName()
    # print("The",lastName,"family:")
    # print(r.returnRandomFirstName("m"),lastName)
    # print(r.returnRandomFirstName("f"),lastName)
    # print(r.returnRandomFirstName("i"),lastName)
    # print(r.returnRandomFirstName("i"),lastName)
    # print(r.returnRandomFirstName("i"),lastName)