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


if __name__ == '__main__':
    #Fixes Screen Flickering:
    os.system("")

    COLOR = {
        "HEADER": "\033[95m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "Black": "\u001b[30m",
        "Yellow": "\u001b[33m",
        "Magenta": "\u001b[35m",
        "Cyan": "\u001b[36m",
        "White": "\u001b[37m",
        "END": "\033[0m",
    }

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


    #GameWindowLoop
    exitFlag =False
    starttime = time.time()
    fps = 0
    fpsflag = 0
    consoleWidth = os.get_terminal_size().lines-2
    consoleHeight = os.get_terminal_size().columns
    consoleManager = GameWindow()

    playerx = 0
    playery = 0
    movementTimer = time.time()
    movementflag = .2
    while (exitFlag == False):
        consoleWidth = os.get_terminal_size().lines-2
        consoleHeight = os.get_terminal_size().columns
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

        drawnStringForConsole = a.returnMapStringCharacters(a.getMap())
        if time.time() < starttime + 1:
            fpsflag += 1
        else:
            fps = fpsflag
            fpsflag = 0
            starttime = time.time()

        #print(drawnStringForConsole)


        print(consoleManager.returnRefreshedScreenString(consoleWidth,consoleHeight,fps,playerx,playery))
        #print("*FPS:",fps,"\033[H\033[3J", end="")
        # Clears the Screen avoiding screen flickering
        #print("\033[H\033[3J", end="")



    print("Console is ",consoleWidth," by ",consoleHeight)
    print(COLOR["Yellow"], "finished", COLOR["END"],sep = "")
    print(COLOR["Black"], "finished", COLOR["END"],sep = "")
    print(COLOR["BLUE"], "finished", COLOR["END"],sep = "")


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