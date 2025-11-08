class GameWindow():

    screenMapString = []
    def __init__(self):
        pass

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

        for i in range (0,width-1):
            for j in range (0,height-1):
                self.screenMapString[i][j] = " "
                if i == 0 or i == width-2:
                    self.screenMapString[i][j] = "═"
                if j == 0 or j == height-2:
                    self.screenMapString[i][j] = "║"
                if i == 0 and j == 0:
                    self.screenMapString[i][j] = "╔"
                if i == width-2 and j == 0:
                    self.screenMapString[i][j] = "╚"
                if i == 0 and j == height-2:
                    self.screenMapString[i][j] = "╗"
                if i == width-2 and j == height-2:
                    self.screenMapString[i][j] = "╝"
                if i == playerx and j == playery:
                    self.screenMapString[i][j] = "X"

        Output = ""
        for i in range(self.width):
            for j in range(self.height):
                Output += str(self.screenMapString[i][j])
            if j < self.height-1:
                Output += str("\n")
        Output += str("\nFPS:"+str(fps)+"\033[H\033[3J")
        return Output
