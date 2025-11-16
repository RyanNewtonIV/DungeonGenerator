import random
from random import Random
import time
from mapGenerator import GameMap, CaveMap
from randomNameGenerator import RandomNameGenerator
import os
import sys
import keyboard
from windowsConsoleGraphics import AsciiArtGenerator, AsciiCharacter
import threading
import asyncio


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


def initializeGameWindowDictFast(char):
    for key in screenBuffer:
        screenBuffer[key].reInitialize(char)

def drawGameWindowBorders():
    pass

def returnFrameStringFromDict(dictionaryToConvert):
    stringArray = []

    for j in range(0, consoleHeight):
        for i in range(0, consoleWidth):

            indexAsciiObject = str(i) + "," + str(j)
            stringArray.append(dictionaryToConvert[indexAsciiObject].getCharacterString())

        if j < consoleHeight - 1:
            #frameString += str("\n")
            stringArray.append("\n")

    stringArray.append("\033[H\033[3J\033[0m")
    frameString = "".join(stringArray)
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

def drawArraytoDict(arrayToDraw, dictToDrawTo):
    for i in arrayToDraw:
        if i.getPropertiesDict()["backgroundColor"] == "Trans":
            i.getPropertiesDict()["backgroundColor"] = dictToDrawTo[i.getDictIndexString()].getPropertiesDict()["backgroundColor"]
        dictToDrawTo[i.getDictIndexString()] = i

def statusBarGetClampedValue(maxstat,clampingAmount,maxWidth):
    if maxstat < clampingAmount:
        return int(maxWidth*(maxstat/clampingAmount))
    else:
        return int(maxWidth)

def returnFrameTimeString(processLabelString):
        processTime = time.time()-timeKeeper
        framePercentage = processTime/(1/fps)*100
        return f"{processLabelString}: {framePercentage:.1f}% | {processTime:,.4f}(s)"


def drawStringToDictExt(dict,string,x,y,alignH,alighV,wrapFlag):
    pass

def getLatencyString():
    pass

def printScreenBuffer():
    sys.stdout.write(returnFrameStringFromDict(screenBuffer))
    sys.stdout.flush()





if __name__ == '__main__':
    #Fixes Screen Flickering:
    os.system("")

    print(sys.path)
    print(os.getcwd())
    timeKeeper = time.time()
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
    fps = 1
    fpsflag = 0
    HeightOffset = 0
    WidthOffset = 0
    consoleHeight = os.get_terminal_size().lines-HeightOffset
    consoleWidth = os.get_terminal_size().columns-WidthOffset
    consoleMidX = int(consoleWidth/2)
    consoleMidY = int(consoleHeight/2)
    asciiArtist = AsciiArtGenerator()
    playerx = 0
    playery = 0
    movementTimer = time.time()
    movementflag = .2
    lagTest = time.time()

    #UI Status Bar Arguments
    UIstatusBarMaxWidth = int(consoleWidth/2)-2
    UImaxHPBarAmountClamping = 1000
    UImaxMPBarAmountClamping = 1000
    UImaxStBarAmountClamping = 1000
    UIStatusBarScalingWidth = 1

    #Player Variables
    maxhp = 320
    hp = 100
    maxmp = 80
    mp = 50
    maxst = 120
    st = 100
    numberOfSouls = 0

    quicktimeTicker = 0


    #Dividor for the number of vertical characters to scale the status bars
    statusbarsScalingFactor = 36
    #How Many lines on the y axis to have for the status bars
    scalingStatusbars = int((statusbarsScalingFactor + consoleHeight) / statusbarsScalingFactor)



    #Slowly Clear the Screen first so hack for redrawing frames works
    cls()

    #Initizalize the Screen Buffer Dictionary
    screenBuffer = initializeGameWindowDict()

    #Variables for Handling the fluctuating frame rate.
    #Multiplier to be paired with actions that happen over a certain number of frames
    timeFPSModifier = 0
    #Time Variables
    time1 = time.time()
    time2 = time.time()

    frameInfoStrings = []

    #Toggles drawing the latency for certain methods
    showLatencyValues = True




    #PRIMARY GAME LOOP
    while (exitFlag == False):


        #threading.Thread(target=printScreenBuffer(), daemon=True)

        #Variables for Time Related modifications with variable frame rates
        time2 = time.time()
        modifierTimer = time2 - time1
        time1 = time2


        timeKeeper = time.time()

        #Flag Console Resize and Clear Screen
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
        else:
            initializeGameWindowDictFast(" ")
        frameInfoStrings.append(returnFrameTimeString("Initialize the Console"))


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
        #drawDicttoDict(asciiArtist.createRectangleDictExt(0,0,consoleWidth,consoleHeight," ","Trans","Trans","doubleLine","Wht","Trans"),screenBuffer)
        drawArraytoDict(asciiArtist.createRectangleBorderArray(0, 0, consoleWidth, consoleHeight, "doubleLine","Wht", "Trans"),screenBuffer)
        #print(asciiArtist.createRectangleBorderArray(0, 0, consoleWidth, consoleHeight, "doubleLine","Wht", "Trans"))
        #time.sleep(2)

        #Draw the Heatlh Bar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2, statusBarGetClampedValue(maxhp, UImaxHPBarAmountClamping, consoleMidX - 2), scalingStatusbars, hp, maxhp, "Red","|","DkGry","Bk-Blk"),screenBuffer)

        # Draw the Mana Bar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2 + scalingStatusbars,statusBarGetClampedValue(maxmp, UImaxMPBarAmountClamping,consoleMidX - 2), scalingStatusbars, mp,maxmp, "Blu", "|", "DkGry", "Bk-Blk"), screenBuffer)

        # Draw the Stamina Bar
        drawDicttoDict(asciiArtist.createStatusBar(2, 2 + scalingStatusbars * 2,statusBarGetClampedValue(maxst, UImaxStBarAmountClamping,consoleMidX - 2), scalingStatusbars, st,maxst, "Grn", "|", "DkGry", "Bk-Blk"), screenBuffer)

        #Draw the Inventory
        drawDicttoDict(asciiArtist.createRectangleDictExt(2,consoleHeight-12,5,5,"█","Blk","Bk-Blk","singleLine","DkGry","Bk-Blk"),screenBuffer)
        drawDicttoDict(asciiArtist.createRectangleDictExt(8, consoleHeight - 17, 5, 5, "█", "Blk", "Bk-Blk","singleLine","DkGry","Bk-Blk"), screenBuffer)
        drawDicttoDict(asciiArtist.createRectangleDictExt(14, consoleHeight - 12, 5, 5, "█", "Blk", "Bk-Blk","singleLine","DkGry","Bk-Blk"), screenBuffer)
        drawDicttoDict(asciiArtist.createRectangleDictExt(8, consoleHeight - 7, 5, 5, "█", "Blk", "Bk-Blk","singleLine","DkGry","Bk-Blk"), screenBuffer)

        #Draw a Sword Hack
        drawDicttoDict(asciiArtist.createStringDict("\\",16,consoleHeight-11,"Wht","Trans"),screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("║", 16, consoleHeight - 10, "Wht", "Trans"),screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("T", 16, consoleHeight - 9, "Wht", "Trans"),screenBuffer)

        # Draw a Shield Hack
        drawDicttoDict(asciiArtist.createStringDict("|", 3, consoleHeight - 10, "Wht", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("_", 4, consoleHeight - 11, "Wht", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("░", 4, consoleHeight - 10, "Wht", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("|", 5, consoleHeight - 10, "Wht", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("v", 4, consoleHeight - 9, "Wht", "Trans"), screenBuffer)

        # Draw Estus Flask Hack
        drawDicttoDict(asciiArtist.createStringDict("_", 10, consoleHeight - 6, "LtYel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("/", 9, consoleHeight - 5, "LtYel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("█", 10, consoleHeight - 5, "Yel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("\\", 11, consoleHeight - 5, "LtYel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("└", 9, consoleHeight - 4, "LtYel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("▀", 10, consoleHeight - 4, "Yel", "Trans"), screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict("┘", 11, consoleHeight - 4, "LtYel", "Trans"), screenBuffer)


        #Draw the Quicktime Event Bar
        drawDicttoDict(asciiArtist.createRectangleDictExt(consoleMidX-22,consoleMidY-scalingStatusbars-1,44, scalingStatusbars+5," ","Wht","Trans","solidBlockSquare","DkGry","Trans"),screenBuffer)
        drawDicttoDict(asciiArtist.createStatusBar(consoleMidX-20,consoleMidY-scalingStatusbars,40, scalingStatusbars+3, quicktimeTicker,100, "Blu", " ", "Trans", "Trans"), screenBuffer)

        #Test the Healthbar
        hp -= 40*modifierTimer
        if hp < 0:
            hp = maxhp
        mp -= 200*modifierTimer
        if mp < 0:
            mp = maxmp
        st -= 80*modifierTimer
        if st < 0:
            st = maxst
        if st > maxst:
            st = 0
        quicktimeTicker += 100*modifierTimer
        if quicktimeTicker > 100:
            quicktimeTicker = 0

        numberOfSouls += 10
        soulsString = "Souls: "+str(numberOfSouls)
        UISoulsDrawAnchorX = consoleWidth-len(soulsString)-4
        UISoulsDrawAnchorY = consoleHeight - 4
        drawDicttoDict(asciiArtist.createRectangleDictExt(UISoulsDrawAnchorX,UISoulsDrawAnchorY,len(soulsString)+2,3,"█","Blk","Trans","singleLine","Wht","Bk-Blk"),screenBuffer)
        drawDicttoDict(asciiArtist.createStringDict(soulsString,UISoulsDrawAnchorX+1,UISoulsDrawAnchorY+1,"Wht","Bk-Blk"),screenBuffer)


        #Handling Calculating and Drawing FPS
        if time.time() < starttime + 1:
            fpsflag += 1
        else:
            fps = fpsflag
            fpsflag = 0
            starttime = time.time()
        fpsString = "|FPS:"+str(fps) + "|" + str(consoleWidth) +"x" + str(consoleHeight)+"|"+str(consoleWidth*consoleHeight)+"units|"
        fpsDict = asciiArtist.createStringDict(fpsString,1,consoleHeight-1,"Wht","Bk-Blk")
        drawDicttoDict(fpsDict,screenBuffer)


        #Draw Latency Calculations
        if (showLatencyValues):
            counter = 0
            for i in range(0,len(frameInfoStrings)):
                drawStringToDict(screenBuffer,frameInfoStrings.pop(0),2,9+counter)
                counter += 1
            drawStringToDict(screenBuffer, f"Total Frame Time: {modifierTimer:,.4f}", 2, 9+counter)


        timeKeeper = time.time()
        #Print Screen Buffer to Console
        screenBufferString = returnFrameStringFromDict(screenBuffer)
        frameInfoStrings.append(returnFrameTimeString("String Conversion"))

        timeKeeper = time.time()
        sys.stdout.write(screenBufferString)
        sys.stdout.flush()
        frameInfoStrings.append(returnFrameTimeString("Outputting to the Console"))









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