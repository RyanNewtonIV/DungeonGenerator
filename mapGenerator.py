from random import Random
import math
import time


# class Vector():
#    coordinate = []
#
#     def __init__(self,x,y):
#        self.coordinate.append(x)
#        self.coordinate.append(y)
#
#     def getX(self):
#        return self.coordinate[0]
#
#     def getY(self):
#        return self.coordinate[1]
#
# class MapPoint(Vector):
#    id = None
#
#     def __init__(self,x,y,id):
#        self.id = id
#        super().__init__(x,y)
#
#     def getID(self):
#        return self.id

class PathFindingNode():
    isObstacle = False
    isVisited = False
    globalDistance = False
    LocalDistance = False
    x = 0
    y = 0
    neighborNodes = []
    parentNode = False


class GameMap():
    mapName = None
    seed = None
    width = None
    height = None
    cellMap = []
    holeSize = 0
    holeSizesMap = []
    entryPoints = []
    exitPoints = []
    randomNumberGenerator = None

    def __init__(self, mapName, seed, width, height,entryPoints,exitPoints):
        self.mapName = mapName
        self.seed = seed
        self.width = width
        self.height = height
        self.entryPoints = entryPoints
        self.exitPoints = exitPoints
        self.randomNumberGenerator = Random()
        self.randomNumberGenerator.seed(self.seed)

    # def initializeEmptyMap(self):
    #     self.cellMap = []
    #     for i in range (self.width):
    #         tempMap = []
    #         for j in range (self.height):
    #             tempMap.append(1)
    #         self.cellMap.append(tempMap)

    def initializeEmptyMap(self,mapToInitialize):
        mapToInitialize = []
        for i in range (self.width):
            tempMap = []
            for j in range (self.height):
                tempMap.append(1)
            mapToInitialize.append(tempMap)

        return mapToInitialize

    def addMap(self,mapToWrite,startx,starty,width,height):
        for i in range(startx,startx+width):
            for j in range(starty,starty+height):
                self.cellMap[i][j] = mapToWrite[i-startx][j-starty]
                #print(mapToWrite[i-startx][j-starty])


    def generateMap(self):
        self.cellMap = self.initializeEmptyMap(self.cellMap)
        self.fillEdges()
        self.mapEntryPoints()
        self.mapExitPoints()
        self.exportMap(self.mapName)
        return self.cellMap

    def returnListofPathCoordinates(self,singleEntryPoint,singleExitPoint):
        pass

    def getMap(self):
        return self.cellMap

    def fillEdges(self):
        for i in range(self.width):
            for j in range(self.height):
                if (i == 0 or j == 0 or i == self.width - 1 or j == self.height - 1):
                    self.cellMap[i][j] = 0

    def fillMap(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cellMap[i][j] = 0

    def fillRectangle(self,mapToFill,indexStartX,indexStartY,indexEndX,indexEndY,fillValue):
        for i in range(indexStartX,indexEndX+1):
            for j in range(indexStartY,indexEndY+1):
                mapToFill[i][j] = fillValue

    def printMapValues(self,mapToPrint):
        for j in range(len(mapToPrint[0])):
            for i in range(len(mapToPrint)):
                print(mapToPrint[i][j], end="")
            print()

    def printMap(self,mapToPrint):
        mapOutput = ""
        for j in range(len(mapToPrint[0])):
            for i in range(len(mapToPrint)):
                if (mapToPrint[i][j] == 0):
                    mapOutput += "█"
                else:
                    mapOutput += " "
            mapOutput += "\n"
        print(mapOutput)
        return mapOutput

    def returnMapStringCharacters(self,mapToPrint):
        mapOutput = ""
        for j in range(len(mapToPrint[0])):
            for i in range(len(mapToPrint)):
                if (mapToPrint[i][j] == 0):
                    mapOutput += "█"
                else:
                    mapOutput += " "
            mapOutput += "\n"
        return mapOutput

    def exportMap(self,fileName):
        mapOutput = open(("Maps/"+fileName+".txt"),"w",encoding="utf-8")
        output = self.printMap(self.cellMap)
        mapOutput.write(output)
        mapOutput.close()
        return self.cellMap

    def mapEntryPoints(self):
        for i in range(len(self.entryPoints)):
            entryPoint = self.entryPoints[i]
            self.cellMap[entryPoint[0]][entryPoint[1]] = 1

    def mapExitPoints(self):
        for i in range(len(self.exitPoints)):
            exitPoint = self.exitPoints[i]
            self.cellMap[exitPoint[0]][exitPoint[1]] = 1

    def copyMap(self,mapToCopy):
        newMap = []
        for i in range(len(mapToCopy)):
            tempMap = []
            for j in range(len(mapToCopy[0])):
                tempMap.append(mapToCopy[i][j])
            newMap.append(tempMap)
        return newMap

    def resetMapValues(self,mapToReset):
        for i in range(len(mapToReset)):
            for j in range(len(mapToReset[0])):
                if (mapToReset[i][j] > 1):
                    mapToReset[i][j] = 1

    def returnTrueIfNeighborValueGreaterThan(self,mapToCheck,x,y,valueToCheck):
        if mapToCheck[x][y] > valueToCheck:
            return True
        return False

    def returnTrueIfAllNeighborsValuesGreaterThan(self, mapToCheck, x, y, valueToCheck):
        if (x == 0 or y == 0 or x == len(mapToCheck) - 1 or y == len(mapToCheck[0]) - 1):
            return False
        if (self.returnTrueIfNeighborValueGreaterThan(mapToCheck,x-1,y,valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck,x+1,y,valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck,x,y-1,valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck, x, y+1, valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck, x-1, y - 1, valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck, x-1, y + 1, valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck, x+1, y + 1, valueToCheck) and
            self.returnTrueIfNeighborValueGreaterThan(mapToCheck,x+1,y-1,valueToCheck)):
                return True
        return False


    def generateFillMap(self):
        fillMap = self.copyMap(self.cellMap)
        self.resetMapValues(fillMap)
        #self.printMapValues(fillMap)

        cellsToProcess = []
        cellsToContinueProcessing = []
        fillIndexValue = 0

        for i in range(len(fillMap)):
            for j in range(len(fillMap[0])):
                if fillMap[i][j] > fillIndexValue:
                    #print("Adding ",i,",",j)
                    cellsToProcess.append([i,j])
                    cellsToContinueProcessing.append([i, j])

        numberOfLoops = 1
        while(len(cellsToContinueProcessing) > 0):
            cellsToContinueProcessing = []
            while(len(cellsToProcess)>0):
                currentCell = cellsToProcess.pop(0)
                if self.returnTrueIfAllNeighborsValuesGreaterThan(fillMap, currentCell[0], currentCell[1], fillIndexValue):
                    fillMap[currentCell[0]][currentCell[1]] += 1
                    cellsToContinueProcessing.append(currentCell)

            #self.printMapValues(fillMap)
            fillIndexValue += 1

            for i in range(len(cellsToContinueProcessing)):
                #print(cellsToContinueProcessing[i])
                cellsToProcess.append(cellsToContinueProcessing[i])

            #print("End of Loop ",numberOfLoops)
            numberOfLoops += 1


        return fillMap

    # By taking a Fill Map, finding the highest values in each area and then moving outwards
    # we can generate a array that holds each room's set of coordinates as its values
    def generateRoomMap(self, fillMapToUse):
        # Fill function
        None










class CaveMap(GameMap):
    birthLimit = None
    deathLimit = None
    openChance = None
    smoothSteps = None
    minHoleSize = None
    holeSize = 0
    holeSizesMap = []

    def __init__(self, mapName, seed, width, height, birthLimit, deathLimit, openChance, smoothSteps, minHoleSize, entryPoints,exitPoints):
        super().__init__(mapName,seed,width,height,entryPoints,exitPoints)
        self.birthLimit = birthLimit
        self.deathLimit = deathLimit
        self.openChance = openChance
        self.minHoleSize = minHoleSize
        self.smoothSteps = smoothSteps
        self.randomNumberGenerator = Random()
        self.randomNumberGenerator.seed(self.seed)

    def generateMap(self):
        self.cellMap = self.initializeEmptyMap(self.cellMap)

        for i in range(self.width):
            for j in range(self.height):
                if (self.randomNumberGenerator.random()<self.openChance):
                    self.cellMap[i][j] = 1
                else:
                    self.cellMap[i][j] = 0
        self.fillEdges()
        self.exportMap((self.mapName+"BaseMap"))

        for i in range (self.smoothSteps):
            self.doSimulationStep()

        self.exportMap((self.mapName+"Smoothed"+str(self.smoothSteps)+"Steps"))
        self.cleanMap()
        return self.cellMap

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

    def cleanMap(self):
        self.identifyHoles()
        self.fillHoles()
        self.exportMap((self.mapName+"SmallHolesFilled"))
        self.mapEntryPoints()
        self.mapExitPoints()
        self.resetMapValues(self.cellMap)
        self.identifyHoles()
        while (len(self.holeSizesMap)> 1):
            self.resetMapValues(self.cellMap)
            #timeStamp = time.time()
            self.identifyHoles()
            #print("All Holes identified in ", str(time.time() - timeStamp), " sec.")
            self.bridgeSection()
            # self.printMapValues(self.cellMap)
        self.exportMap((self.mapName+"TerrainFinished"))

    def identifyHoles(self):
        holeNumber = 1
        self.holeSizesMap = []
        for i in range(self.width):
            for j in range(self.height):
                if (self.cellMap[i][j] == 1):
                    self.findHoles(i,j,holeNumber+1)
                    self.holeSizesMap.append(self.holeSize)
                    self.holeSize = 0
                    #print(self.holeSizesMap)
                    holeNumber += 1
        # self.printMapValues(self.cellMap)
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

    def findHoles(self,x,y,fillColor):
        vectorsToCheck = [[x,y]]

        while len(vectorsToCheck)>0:
            coordinateChecking = vectorsToCheck.pop(0)
            x = coordinateChecking[0]
            y = coordinateChecking[1]
            loopRunning = self.checkForPaintedHoles(x,y,fillColor)
            if not loopRunning:
                self.holeSize += 1
                self.cellMap[x][y] = fillColor
                if x < self.width-1:
                    if not self.checkForPaintedHoles(x+1,y,fillColor):
                        vectorsToCheck.append([x+1,y])
                if x>0:
                    if not self.checkForPaintedHoles(x-1,y,fillColor):
                        vectorsToCheck.append([x-1,y])
                if y< self.height-1:
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

#1/27/22 - This Class needs to take a number of different regions and allowed mapTypes(Biomes) to make a combined and interesting area
class CombinedMap(GameMap):

    differentRegions = None
    allowedMapTypes = []

    def __init__(self, mapName, seed, width, height, entryPoints,exitPoints, differentRegions, allowedMapTypes):
        super().__init__(mapName, seed, width, height, entryPoints, exitPoints)
        self.differentRegions = differentRegions
        self.allowedMapTypes = allowedMapTypes

    def generateMap(self):
        self.cellMap = self.initializeEmptyMap(self.cellMap)


# class MazeMap(GameMap):
#
#     def __init__(self, mapName, seed, width, height, entryPoints):
#         super().__init__(mapName,seed,width,height,entryPoints)
#
#     def getMap(self):
#         self.initializeEmptyMap()
#         self.fillEdges()
#         self.mapEntryPoints()
#         self.generateMaze()
#         self.exportMap(self.mapName)
#         return self.cellMap
#
#     def generateMaze(self):
#         wallsToAnalyze = self.generatePointstoAnalyze()
#         while wallsToAnalyze != []:
#             wallsToAnalyze = self.makeRandomMazeWalls(wallsToAnalyze)
#
#     def generateInitialPointstoAnalyze(self):
#         wallsToAnalyze = []
#         for i in range(self.width):
#             for j in range(self.height):
#                 if (i == 0 or i == self.width - 1):
#                     if (j != 0 and j != self.height-1 and j%2 == 0):
#                         if (self.cellMap[i][j] == 0):
#                             wallsToAnalyze.append([i,j])
#                 elif (j == 0 or j == self.height - 1):
#                     if (i != 0 and i != self.height-1 and i%2 == 0):
#                         if (self.cellMap[i][j] == 0):
#                             wallsToAnalyze.append([i,j])
#         return wallsToAnalyze
#
#     def makeRandomMazeWalls(self,wallsToAnalyze):
#         for i in range(wallsToAnalyze):
#             if (self.randomNumberGenerator.randint(0,1) == 1):
#                 if (i[0] == 0):
#
#
#                 elif (i[0] == self.width-1):
#
#                 elif (i[1] == 0):
#
#                 elif (i[1] == self.height - 1):
#
#                 else:
