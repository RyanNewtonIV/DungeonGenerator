class GameWindow():

    screenMapString = []

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
        "Whi": "[97m",
        "Bk-Whi": "[107m",
        "Bold": "[1m",
        "Underline": "[4m",
        "END": "[0m"


    }


    def drawRectangle(self,x,y,width,height,fill,borderType):

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

    def __init__(self):
        pass

    def colTxt(self,string,color):
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
