import random
from random import Random
import time
from mapGenerator import GameMap, CaveMap
from randomNameGenerator import RandomNameGenerator
import os
import sys
import keyboard
from windowsConsoleGraphics import AsciiArtGenerator, AsciiCharacter


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
            # index = random.randint(0,5)
            # if index < 3:
            #     newCharacter = AsciiCharacter(i,j,"*","Wht","Trans",False,False)
            # elif index == 5:
            #     newCharacter = AsciiCharacter(i, j, "O", "Blu", "Trans", False, False)
            # else:
            #     newCharacter = AsciiCharacter(i, j, "X", "Red", "Bk-Blk", False, False)
            newCharacter = AsciiCharacter(i, j, ".", "DkGry", "Trans", False, False)
            gameWindowDict[indexString] = newCharacter

    return gameWindowDict

def drawGameWindowBorders():
    pass

def returnFrameStringFromDict(dictionaryToConvert):
    frameString = ""

    for j in range(0, consoleHeight):
        for i in range(0, consoleWidth):

            indexAsciiObject = str(i) + "," + str(j)
            frameString += dictionaryToConvert[indexAsciiObject].getCharacterString()

            # Broken attempt at optomization
            # if i != 0 and j != 0:
            #     if i > 0:
            #         prevIndexAsciiObject = str(i-1) + "," + str(j)
            #     else:
            #         frameString += dictionaryToConvert[indexAsciiObject].getCharacterString()
            #         pass
            #
            #     if dictionaryToConvert[indexAsciiObject].getProperties() == dictionaryToConvert[prevIndexAsciiObject].getProperties():
            #         frameString += dictionaryToConvert[indexAsciiObject].getCharacterSimple()
            #     else:
            #         frameString += dictionaryToConvert[indexAsciiObject].getCharacterString()
            # else:
            #     frameString += dictionaryToConvert[indexAsciiObject].getCharacterString()


        if j < consoleHeight - 1:
            frameString += str("\n")


    frameString += str("\033[H\033[3J\033[0m")
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
        newCharacter = AsciiCharacter(x+i,y,string[i],"Wht","Trans",False,False)
        screenBuffer[indexString] = newCharacter
    return dict

def drawDicttoDict(dictToDraw, dictToDrawTo):

    xstart = dictToDraw['x']
    ystart = dictToDraw['y']
    width = dictToDraw['width']
    height = dictToDraw['height']

    for j in range(ystart,height+ystart):
        for i in range(xstart,width+xstart):
            indexString = str(i) + "," + str(j)
            if dictToDraw[indexString].getCharacterSimple() != " ":
                if dictToDraw[indexString].getPropertiesDict()["backgroundColor"] == "Trans":
                    dictToDraw[indexString].getPropertiesDict()["backgroundColor"] = dictToDrawTo[indexString].getPropertiesDict()["backgroundColor"]
                dictToDrawTo[indexString] = dictToDraw[indexString]



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
    consoleMidX = consoleWidth/2
    consoleMidY = consoleHeight/2
    statusbarsScalingFactor = 36
    scalingStatusbars = int((statusbarsScalingFactor + consoleHeight) / statusbarsScalingFactor)
    asciiArtist = AsciiArtGenerator()
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

    rectangleDict = asciiArtist.createRectangleDict(5, 5, 10, 10, " ", "Red", "Trans")
    rectangleDict = asciiArtist.createRectangleDictExt(5, 5, 10, 10, " ", "Red", "Trans", "solidBlockSquareRoundedCorners", "Wht", "Trans")
    #drawDicttoDict(rectangleDict,screenBuffer,rectangleDict['x'],rectangleDict['y'],rectangleDict['width'],rectangleDict['height'])
    drawDicttoDict(rectangleDict, screenBuffer)

    maxhp = 100
    hp = 100

    #PRIMARY GAME LOOP
    while (exitFlag == False):

        screenBuffer = initializeGameWindowDict()

        #Flag Console Resize
        if (flagConsoleResize(consoleWidth,consoleHeight)):
            testvar = os.get_terminal_size().lines - HeightOffset
            if consoleHeight != testvar:
                consoleHeight = testvar
                consoleMidY = int(testvar / 2)
                scalingStatusbars = int((statusbarsScalingFactor + consoleHeight) / statusbarsScalingFactor)
                cls()
            testvar = os.get_terminal_size().columns - WidthOffset
            if consoleWidth != testvar:
                consoleWidth = testvar
                consoleMidX = int(testvar / 2)
                cls()
            screenBuffer = initializeGameWindowDict()

        #Input Handling
        try:
            if keyboard.is_pressed('Esc'):
                print("\n\x1B[0myou pressed Esc, so exiting...")
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

        #Draw the Game Window Borders
        drawDicttoDict(asciiArtist.createRectangleDictExt(0,0,consoleWidth,consoleHeight," ","Trans","Trans","doubleLine","Wht","Trans"),screenBuffer)

        #Draw the Healthbar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2, int(consoleMidX-2), scalingStatusbars, hp, maxhp, "Red","░","DkGry","Bk-Blk"),screenBuffer)
        # Draw the Manabar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2+scalingStatusbars, int(consoleMidX - 2), scalingStatusbars, hp, maxhp, "Blu", "░", "DkGry","Bk-Blk"), screenBuffer)
        # Draw the Manabar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2 + scalingStatusbars*2, int(consoleMidX - 2), scalingStatusbars, hp, maxhp,"Grn", "░", "DkGry", "Bk-Blk"), screenBuffer)

        #Test the Healthbar
        hp -= .1
        if hp < 0:
            hp = maxhp


        #Handling Calculating and Drawing FPS
        if time.time() < starttime + 1:
            fpsflag += 1
        else:
            fps = fpsflag
            fpsflag = 0
            starttime = time.time()
        fpsString = "|FPS:"+str(fps) + "|" + str(consoleWidth) +"x" + str(consoleHeight)+"|"+str(consoleWidth*consoleHeight)+"units|"
        #drawStringToDict(screenBuffer,fpsString,1,consoleHeight-1)
        fpsDict = asciiArtist.createStringDict(fpsString,1,consoleHeight-1,"Wht","Bk-Blk")
        drawDicttoDict(fpsDict,screenBuffer)
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