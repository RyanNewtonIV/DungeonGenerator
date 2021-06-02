import random
import math
import time

class Vector():
    x = None
    y = None

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class MapPoint(Vector):
    id = None

    def __init__(self,x,y,id):
        self.id = id
        super().__init__(x,y)

    def getID(self):
        return self.id

class CaveMap():
    mapName = None
    seed = None
    height = None
    width = None
    birthLimit = None
    deathLimit = None
    openChance = None
    smoothSteps = None
    cellMap = []
    minHoleSize = None
    holeSize = 0
    holeSizesMap = []
    entryPoints = []
    randomNumberGenerator = None

    def __init__(self, mapName, seed, width, height, birthLimit, deathLimit, openChance, smoothSteps, minHoleSize, entryPoints):
        self.mapName = mapName
        self.seed = seed
        self.width = width
        self.height = height
        self.birthLimit = birthLimit
        self.deathLimit = deathLimit
        self.openChance = openChance
        self.minHoleSize = minHoleSize
        self.smoothSteps = smoothSteps
        self.entryPoints = entryPoints
        self.randomNumberGenerator = random.Random()
        self.randomNumberGenerator.seed(self.seed)
        for i in range (width):
            tempMap = []
            for j in range (height):
                tempMap.append(0)
            self.cellMap.append(tempMap)

        for i in range(self.width):
            for j in range(self.height):
                if (self.randomNumberGenerator.random()<openChance):
                    self.cellMap[i][j] = 1
                else:
                    self.cellMap[i][j] = 0

        self.fillEdges()

        self.exportMap((mapName+"BaseMap"))
        #self.printMap()
        #self.printMapValues()

        for i in range (self.smoothSteps):
            self.doSimulationStep()

        #self.printMap()
        #self.printMapValues()

        self.exportMap((mapName+"Smoothed"+str(smoothSteps)+"Steps"))
        self.cleanMap()

    def fillEdges(self):
        for i in range(self.width):
            for j in range(self.height):
                if (i == 0 or j == 0 or i == self.width - 1 or j == self.height - 1):
                    self.cellMap[i][j] = 0

    def printMapValues(self):
        for j in range (self.height):
            for i in range (self.width):
                print(self.cellMap[i][j], end="")
            print()

    def printMap(self):
        mapOutput = ""
        for i in range(self.height):
            for j in range(self.width):
                if (self.cellMap[j][i] == 0):
                    mapOutput += "█"
                else:
                    mapOutput += " "
            mapOutput +="\n"
        print(mapOutput)
        return mapOutput

    def getEmptyNeighbors(self,x,y):
        numberOfEmptyNeighbors = 0
        if (x>0 and x<self.width-1 and y>0 and y<self.height-1):
            for i in range (-1,2):
                for j in range(-1, 2):
                    if (i==0 and j==0):
                        pass
                    elif (self.cellMap[x+i][y+j]>0):
                        numberOfEmptyNeighbors += 1
        return numberOfEmptyNeighbors

    def doSimulationStep(self):
        newMap = []
        for i in range (self.width):
            tempMap = []
            for j in range (self.height):
                tempMap.append(0)
            newMap.append(tempMap)

        for x in range (1,self.width-1):
            for y in range (1,self.height-1):
                numberOfAliveNeighbors = self.getEmptyNeighbors(x,y)
                if (self.cellMap[x][y] == 1):
                    if (numberOfAliveNeighbors > self.deathLimit):
                        newMap[x][y] = 1
                    else:
                        newMap[x][y] = 0
                else:
                    if numberOfAliveNeighbors > self.birthLimit:
                        newMap[x][y]=1
                    else:
                        newMap[x][y]=0

        for i in range(self.width):
            for j in range(self.height):
                self.cellMap[i][j] = newMap[i][j]

    def exportMap(self,fileName):
        mapOutput = open((fileName+".txt"),"w",encoding="utf-8")
        output = self.printMap()
        mapOutput.write(output)

    def cleanMap(self):
        self.identifyHoles()
        self.fillHoles()
        self.exportMap((self.mapName+"SmallHolesFilled"))
        self.mapEntryPoints()
        while (len(self.holeSizesMap)> 1):
            self.resetHoles()
            #timeStamp = time.time()
            self.identifyHoles()
            #print("All Holes identified in ", str(time.time() - timeStamp), " sec.")
            self.bridgeSection()
            #self.printMapValues()
        self.exportMap((self.mapName+"TerrainFinished"))

    def mapEntryPoints(self):
        for i in range(len(self.entryPoints)):
            entryPoint = self.entryPoints[i]
            self.cellMap[entryPoint[0]][entryPoint[1]] = 1


    def identifyHoles(self):
        holeNumber = 1
        self.holeSizesMap = []
        for i in range(self.width):
            for j in range(self.height):
                if (self.cellMap[i][j] == 1):
                    self.findHoles2(i,j,holeNumber+1)
                    self.holeSizesMap.append(self.holeSize)
                    self.holeSize = 0
                    #print(self.holeSizesMap)
                    holeNumber += 1
        #self.printMapValues()
        print("There are currently ",str(holeNumber-1)," isolated holes on this map.")
        for i in range(len(self.holeSizesMap)):
            pass
            #print("This size of hole #",str(i+2)," is ",str(self.holeSizesMap[i]),".")


    def smoothChannels(self,x,y):
        numberOfAliveNeighbors = self.getEmptyNeighbors(x,y)
        if (numberOfAliveNeighbors > self.birthLimit):
            self.cellMap[x][y] = 1

    def smoothNeighbors(self, x, y):
        self.smoothChannels(x+1,y)
        self.smoothChannels(x+1,y+1)
        self.smoothChannels(x,y+1)
        self.smoothChannels(x-1,y+1)
        self.smoothChannels(x-1,y)
        self.smoothChannels(x-1,y-1)
        self.smoothChannels(x,y-1)
        self.smoothChannels(x+1,y-1)

    def resetHoles(self):
        for i in range(self.width):
            for j in range(self.height):
                if (self.cellMap[i][j] > 1):
                    self.cellMap[i][j] = 1

    def findHoles(self,x,y,fillColor):
        if(self.cellMap[x][y] == fillColor or self.cellMap[x][y] == 0):
            pass
        else:
            self.cellMap[x][y] = fillColor
            self.holeSize += 1
            if (x<self.width-1):
                self.findHoles(x+1,y,fillColor)
            if (y<self.height-1):
                self.findHoles(x,y+1,fillColor)
            if (x>0):
                self.findHoles(x-1,y,fillColor)
            if (y>0):
                self.findHoles(x,y-1,fillColor)

    def findHoles2(self,x,y,fillColor):
        vectorsToCheck = [[x,y]]

        while len(vectorsToCheck)>0:
            coordinateChecking = vectorsToCheck.pop(0)
            x = coordinateChecking[0]
            y = coordinateChecking[1]
            loopRunning = self.checkForPaintedHoles(x,y,fillColor)
            if not loopRunning:
                self.holeSize += 1
                self.cellMap[x][y] = fillColor
                if x < width-1:
                    if not self.checkForPaintedHoles(x+1,y,fillColor):
                        vectorsToCheck.append([x+1,y])
                if x>0:
                    if not self.checkForPaintedHoles(x-1,y,fillColor):
                        vectorsToCheck.append([x-1,y])
                if y<height-1:
                    if not self.checkForPaintedHoles(x,y+1,fillColor):
                        vectorsToCheck.append([x,y+1])
                if y>0:
                    if not self.checkForPaintedHoles(x,y-1,fillColor):
                        vectorsToCheck.append([x,y-1])


    def checkForPaintedHoles(self,x,y,fillColor):
        if (self.cellMap[x][y] == fillColor or self.cellMap[x][y] == 0):
            return True
        else:
            return False

    def fillHoles(self):
        for i in range(self.width):
            for j in range(self.height):
                if (self.cellMap[i][j] > 1):
                    if self.holeSizesMap[self.cellMap[i][j] - 2]< self.minHoleSize:
                        self.cellMap[i][j] = 0

    def bridgeSection(self):
        if (len(self.holeSizesMap) > 1):
            bridgeStartx = 0
            bridgeStarty = 0
            bridgeEndx = self.width-1
            bridgeEndy = self.height-1
            bridgeDistance = self.width+self.height

            #self.printMapValues()
            for i in range(self.width):
                for j in range(self.height):
                    if (self.cellMap[i][j]==len(self.holeSizesMap)+1):
                        for k in range(i-int(bridgeDistance-1),i+int(bridgeDistance+1)):
                            if k >= 0 and k < self.width-1:
                                for l in range(j-int(bridgeDistance-1),j+int(bridgeDistance+1)):
                                    if l >= 0 and l < self.height-1:
                                        if self.cellMap[k][l] > 0:
                                            testId = self.cellMap[i][j]
                                            if self.cellMap[k][l] != testId:
                                                if abs(k-i)<bridgeDistance and abs(l-j) < bridgeDistance:
                                                    testDistance = abs(math.sqrt((k-i)*(k-i)+(l-j)*(l-j)))
                                                    if testDistance<bridgeDistance:
                                                        bridgeStartx=i
                                                        bridgeStarty=j
                                                        bridgeEndx=k
                                                        bridgeEndy=l
                                                        bridgeDistance=testDistance
                                                        #print("New bridge found with distance: ",str(bridgeDistance))
            bridgeConstructorx = bridgeStartx
            bridgeConstructory = bridgeStarty
            self.cellMap[bridgeConstructorx][bridgeConstructory]=1
            self.smoothNeighbors(bridgeConstructorx,bridgeConstructory)
            while bridgeConstructorx != bridgeEndx or bridgeConstructory != bridgeEndy:
                self.cellMap[bridgeConstructorx][bridgeConstructory] = 1
                self.smoothNeighbors(bridgeConstructorx,bridgeConstructory)
                if abs(bridgeConstructorx-bridgeEndx)>abs(bridgeConstructory-bridgeEndy):
                    if bridgeConstructorx>bridgeEndx:
                        bridgeConstructorx -= 1
                    else:
                        bridgeConstructorx += 1
                    if bridgeConstructory > self.height / 2:
                        self.cellMap[bridgeConstructorx][bridgeConstructory - 1] = 1
                        for i in range(3):
                            self.smoothNeighbors(bridgeConstructorx, bridgeConstructory - 1)
                    else:
                        self.cellMap[bridgeConstructorx][bridgeConstructory + 1] = 1
                        for i in range(3):
                            self.smoothNeighbors(bridgeConstructorx, bridgeConstructory + 1)
                else:
                    if bridgeConstructory>bridgeEndy:
                        bridgeConstructory-=1
                    else:
                        bridgeConstructory+=1
                    if bridgeConstructorx>self.width/2:
                        self.cellMap[bridgeConstructorx-1][bridgeConstructory] = 1
                        for i in range(3):
                            self.smoothNeighbors(bridgeConstructorx-1,bridgeConstructory)
                    else:
                        self.cellMap[bridgeConstructorx+1][bridgeConstructory] = 1
                        for i in range(3):
                            self.smoothNeighbors(bridgeConstructorx+1, bridgeConstructory)

if __name__ == '__main__':

    rand = random.Random()
    seed = rand.randint(0, 100000)
    width = 150
    height = 150
    smoothStep = 5
    minRoomSize = 10
    entryPoints = [[rand.randint(0, width - 1), 0],
                   [rand.randint(0, width - 1), height - 1],
                   [width - 1, rand.randint(0, height - 1)],
                   [0, rand.randint(0, height - 1)]]
    a = CaveMap("TestMap", seed, width, height, 4, 3, 0.5, smoothStep, minRoomSize, entryPoints)