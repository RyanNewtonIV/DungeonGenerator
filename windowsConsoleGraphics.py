import time


class AsciiCharacter():

    COLOR = {
        "ESCAPECODE-Octal": "\033",
        "ESCAPECODE-Unicode": "\u001b",
        "ESCAPECODE-Hexadecimal": "\x1B",
        "HEADER": "[95m",
        "Blk": "[30m",
        "Bk-Blk": "[40m",
        "Red": "[31m",
        "Bk-Red": "[41m",
        "Grn": "[32m",
        "Bk-Grn": "[42m",
        "Yel": "[33m",
        "Bk-Yel": "[43m",
        "Blu": "[34m",
        "Bk-Blu": "[44m",
        "Mag": "[35m",
        "Bk-Mag": "[45m",
        "Cyn": "[36m",
        "Bk-Cyn": "[46m",
        "LtGry": "[37m",
        "Bk-LtGry": "[47m",
        "DkGry": "[90m",
        "Bk-DkGry": "[100m",
        "LtRed": "[91m",
        "Bk-LtRed": "[101m",
        "LtGrn": "[92m",
        "Bk-LtGrn": "[102m",
        "LtYel": "[93m",
        "Bk-LtYel": "[103m",
        "LtBlu": "[94m",
        "Bk-LtBlu": "[104m",
        "LtMag": "[95m",
        "Bk-LtMag": "[105m",
        "LtCyn": "[96m",
        "Bk-LtCyn": "[106m",
        "Wht": "[97m",
        "Bk-Whi": "[107m",
        "Bold": "[1m",
        "Underline": "[4m",
        "Trans": "",
        "END": "[0m"
    }



    def __init__(self,x,y,characterString,txtColor,backgroundColor,bold,underline):
        self.properties = {}
        self.properties["x"] = x
        self.properties["y"] = y
        self.properties['charSymbol'] = characterString
        self.properties['txtColor'] = txtColor
        self.properties['backgroundColor'] = backgroundColor
        self.properties['bold'] = bold
        self.properties['underline'] = underline


    def getDictIndexString(self):
        return str(str(self.properties["x"])+","+ str(self.properties["y"]))

    def getPropertiesDict(self):
        return self.properties

    def getCharacterSimple(self):
        return self.properties["charSymbol"]

    def getCharacterString(self):
        if self.properties["bold"] == False and self.properties["underline"]== False:
            if self.properties["backgroundColor"]=="Trans":
                if self.properties["txtColor"]=="Wht":
                    return self.properties["charSymbol"]
                return self.colTxt(self.properties["charSymbol"],self.properties["txtColor"])
        return self.colTxtExt(self.properties["charSymbol"],self.properties["txtColor"],self.properties["backgroundColor"],self.properties["bold"],self.properties["underline"])

    def getPropertiesString(self):
        return str(self.properties["txtColor"])+str(self.properties["backgroundColor"])+str(self.properties["bold"])+str(self.properties["underline"])

    def colTxt(self,string,color):
        return str(self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR[color]+str(string)+self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR["END"])

    def colTxtExt(self,string,textColor,backgroundColor,bold,underline):
        boldstring = ""
        if bold == True:
            boldstring = self.COLOR["ESCAPECODE-Hexadecimal"]+"[1m"
        underlinestring = ""
        if underline == True:
            underlinestring = self.COLOR["ESCAPECODE-Hexadecimal"]+"[4m"
        #return str(self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR[textColor]+self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR[backgroundColor]+boldstring+underlinestring+str(string)+self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR["END"])
        return str(self.COLOR["ESCAPECODE-Hexadecimal"] + self.COLOR[textColor] + self.COLOR["ESCAPECODE-Hexadecimal"] + self.COLOR[backgroundColor] + boldstring + underlinestring + str(string)+self.COLOR["ESCAPECODE-Hexadecimal"] + self.COLOR["END"])



class AsciiArtGenerator():

    screenMapString = []
    def __init__(self):
        pass

    def createStatusBar(self,x,y,width,height,doubleCurrentAmount,doubleAmountMax, fillCharColor, emptyChar, emptyCharColor, charBackgroundColor):

        returnAsciiSpriteDict = {}
        returnAsciiSpriteDict['x'] = x
        returnAsciiSpriteDict['y'] = y
        returnAsciiSpriteDict['width'] = width
        returnAsciiSpriteDict['height'] = height
        amountModifier = doubleCurrentAmount/doubleAmountMax
        numberOfSquares = amountModifier*width
        remainder = numberOfSquares % 1
        numberOfFullSquares = int(numberOfSquares)


        # print("y: ",y)
        # print("width: ",width)
        # print("height: ",height)
        # print("Max Amount: ",doubleAmountMax)
        # print("Current Amount: ",doubleCurrentAmount)
        # print("Percentage: ",amountModifier)
        # print("Percentage x Squares: ",numberOfSquares)
        # print("x: ",x)
        # print("Percentage x Squares rounded: ",numberOfFullSquares)
        # print("Remainder: ",remainder)
        #
        # time.sleep(10)

        for j in range(y, height+y):
            for i in range(x, width+x):
                indexString = str(i) + "," + str(j)
                if i-x < numberOfFullSquares:
                    returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", fillCharColor, charBackgroundColor, False, False)
                elif i-x == numberOfFullSquares:
                    if remainder < .25:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "░", fillCharColor, charBackgroundColor, False, False)
                    elif remainder < .5:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▒", fillCharColor, charBackgroundColor, False, False)
                    elif remainder < .75:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▓", fillCharColor, charBackgroundColor, False, False)
                        # print(returnAsciiSpriteDict[indexString].getPropertiesString())
                        # time.sleep(2)
                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", fillCharColor, charBackgroundColor, False, False)
                else:
                    # returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", fillCharBackgroundColor,fillCharBackgroundColor, False, False)
                    returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, emptyChar, emptyCharColor,charBackgroundColor, False, False)

                # if j > 0:
                #     returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, str(i%10), fillCharBackgroundColor,fillCharBackgroundColor, False, False)

        return returnAsciiSpriteDict

    def createRectangleDict(self, x, y, width, height, fillCharacter, fillCharColor, fillCharBackgroundColor):

        # Create Dictionary containing the Ascii Information
        returnAsciiSpriteDict = {}
        returnAsciiSpriteDict['x'] = x
        returnAsciiSpriteDict['y'] = y
        returnAsciiSpriteDict['width'] = width
        returnAsciiSpriteDict['height'] = height

        for j in range(y, height+y):
            for i in range(x, width+x):
                indexString = str(i) + "," + str(j)
                returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor, fillCharBackgroundColor, False, False)

        return returnAsciiSpriteDict


    def createRectangleBorderArray(self,x, y, width, height, borderType, borderCharColor, borderCharBkColor):
        returnAsciiSpriteArr = []
        xbounds = x + width - 1
        ybounds = y + height - 1

        if borderType == "doubleLine":

            for j in range(y, height + y):
                for i in range(x, width + x):
                    if i == x and j == y:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "╔", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    elif i == xbounds and j == y:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "╗", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    elif i == x and j == ybounds:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "╚", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "╝", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    elif i == x or i == xbounds:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "║", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    elif j == y or j == ybounds:
                        returnAsciiSpriteArr.append(AsciiCharacter(i, j, "═", borderCharColor,
                                                                            borderCharBkColor, False, False))
                    else:
                        pass
            return returnAsciiSpriteArr

    def createRectangleDictExt(self, x, y, width, height, fillCharacter, fillCharColor, fillCharBkColor, borderType, borderCharColor, borderCharBkColor):

        # Create Dictionary containing the Ascii Information
        returnAsciiSpriteDict = {}
        returnAsciiSpriteDict['x'] = x
        returnAsciiSpriteDict['y'] = y
        returnAsciiSpriteDict['width'] = width
        returnAsciiSpriteDict['height'] = height
        xbounds = x+width-1
        ybounds = y+height-1

        if borderType == "doubleLine":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "╔", borderCharColor,
                                                                            borderCharBkColor, False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "╗", borderCharColor,
                                                                            borderCharBkColor, False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "╚", borderCharColor,
                                                                            borderCharBkColor, False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "╝", borderCharColor,
                                                                            borderCharBkColor, False, False)
                    elif i == x or i == xbounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "║", borderCharColor,
                                                                            borderCharBkColor, False, False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "═", borderCharColor,
                                                                            borderCharBkColor, False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,
                                                                            fillCharBkColor, False, False)
            return returnAsciiSpriteDict

        if borderType == "singleLine":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "┌", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "┐", borderCharColor, borderCharBkColor,False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "└", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "┘", borderCharColor, borderCharBkColor,False, False)
                    elif i == x or i == xbounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i,j,"│",borderCharColor,borderCharBkColor,False,False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "─", borderCharColor, borderCharBkColor,False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,fillCharBkColor, False, False)
            return returnAsciiSpriteDict

        if borderType == "solidBlockRoundedCorners":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▄", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▄", borderCharColor, borderCharBkColor,False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▀", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▀", borderCharColor, borderCharBkColor,False, False)
                    elif i == x or i == xbounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i,j,"█",borderCharColor,borderCharBkColor,False,False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,fillCharBkColor, False, False)
            return returnAsciiSpriteDict

        if borderType == "solidBlockSquareRoundedCorners":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, " ", borderCharColor, borderCharBkColor,False, False)
                    elif i == x+1 and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▄", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, " ", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds-1 and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▄", borderCharColor, borderCharBkColor, False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, " ", borderCharColor, borderCharBkColor,False, False)
                    elif i == x+1 and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▀", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, " ", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds-1 and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "▀", borderCharColor, borderCharBkColor,False, False)
                    elif i <= x+1 or i >= xbounds-1:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i,j,"█",borderCharColor,borderCharBkColor,False,False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,fillCharBkColor, False, False)
            return returnAsciiSpriteDict

        if borderType == "solidBlockThinSides":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == x or i == xbounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i,j,"█",borderCharColor,borderCharBkColor,False,False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,fillCharBkColor, False, False)
            return returnAsciiSpriteDict

        if borderType == "solidBlockSquare":

            for j in range(y, height + y):
                for i in range(x, width + x):

                    indexString = str(i) + "," + str(j)

                    if i == x and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == y:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == x and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i == xbounds and j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)
                    elif i <= x+1 or i >= xbounds-1:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i,j,"█",borderCharColor,borderCharBkColor,False,False)
                    elif j == y or j == ybounds:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, "█", borderCharColor, borderCharBkColor,False, False)

                    else:
                        returnAsciiSpriteDict[indexString] = AsciiCharacter(i, j, fillCharacter, fillCharColor,fillCharBkColor, False, False)

            return returnAsciiSpriteDict

        return returnAsciiSpriteDict

    def createStringDict(self, string, x, y, color,bkcolor):

        returnAsciiSpriteDict = {}
        returnAsciiSpriteDict['x'] = x
        returnAsciiSpriteDict['y'] = y
        returnAsciiSpriteDict['width'] = len(string)
        returnAsciiSpriteDict['height'] = 1

        indexString = ""

        for i in range(0,len(string)):
            indexString = str(x + i) + "," + str(y)
            newCharacter = AsciiCharacter(x + i, y, string[i], color, bkcolor, False, False)
            returnAsciiSpriteDict[indexString] = newCharacter

        return returnAsciiSpriteDict



    def createTextDictExt(self,string,color):
        return str(self.COLOR["ESCAPECODE-Octal"]+self.COLOR[color]+str(string)+self.COLOR["END"])

    def colTxtExt(self,string,textColor,backgroundColor,bold,underline):
        boldstring = ""
        if bold == True:
            boldstring = self.COLOR["ESCAPECODE-Hexadecimal"]+"[1m"
        underlinestring = ""
        if underline == True:
            underlinestring = self.COLOR["ESCAPECODE-Hexadecimal"]+"[4m"
        return str(self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR[textColor]+self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR[backgroundColor]+boldstring+underlinestring+str(string)+self.COLOR["ESCAPECODE-Hexadecimal"]+self.COLOR["END"])

    def returnRefreshedScreenString(self,width,height,fps,playerx,playery):

        self.width = width
        self.height = height
        self.fps = fps

        self.screenMapString = []
        for i in range(self.width):
            tempMap = []
            for j in range(self.height):
                tempMap.append(" ")
            self.screenMapString.append(tempMap)

        for j in range (0,height):
            for i in range (0,width):
                self.screenMapString[i][j] = "*"
                if i == 0 or i == width-1:
                    self.screenMapString[i][j] = "║"
                if j == 0 or j == height-1:
                    self.screenMapString[i][j] = "═"
                if i == 0 and j == 0:
                    self.screenMapString[i][j] = "╔"
                if i == width-1 and j == 0:
                    self.screenMapString[i][j] = "╗"
                if i == 0 and j == height-1:
                    self.screenMapString[i][j] = "╚"
                if i == width-1 and j == height-1:
                    self.screenMapString[i][j] = "╝"
                if i == playerx and j == playery:
                    self.screenMapString[i][j] = self.colTxtExt("X","LtBlu","Bk-Blk",False,False)

        Output = ""
        for j in range(self.height):
            for i in range(self.width):
                Output += str(self.screenMapString[i][j])
            if j < self.height-1:
                Output += str("\n")
        Output += str("\nFPS:"+str(fps)+"\033[H\033[3J")
        return Output
