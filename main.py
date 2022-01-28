from random import Random
import time
from mapGenerator import GameMap, CaveMap
from randomNameGenerator import RandomNameGenerator



if __name__ == '__main__':

    timeKepper = time.time()
    rand = Random()
    seed = rand.randint(0, 100000)

    #seed = 15092

    #width = 150
    #height = 14
    width = 150
    height = 10
    #openNess = 0.55
    openNess = .75
    smoothStep = 5
    minRoomSize = 10
    entryPoints = []
    exitPoints = []

    # entryPoints = [[rand.randint(1, width - 2), 0],
    #                [rand.randint(1, width - 2), height - 1],
    #                [width - 1, rand.randint(1, height - 2)],
    #                [0, rand.randint(1, height - 2)]]
    # exitPoints = [[rand.randint(1, width - 2), 0],
    #                [rand.randint(1, width - 2), height - 1],
    #                [width - 1, rand.randint(1, height - 2)],
    #                [0, rand.randint(1, height - 2)]]

    a = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    a.generateMap()
    a.printMap(a.getMap())
    fillMap = a.generateFillMap()
    a.printMapValues(fillMap)
    print("finished")


    # a = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    # seed = rand.randint(0, 100000)
    # b = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    # seed = rand.randint(0, 100000)
    # c = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    # seed = rand.randint(0, 100000)
    # d = GameMap("TestMap", seed, width, height, entryPoints, exitPoints)
    # mapsUsed = [a,b,c,d]
    #
    # for i in range(len(mapsUsed)):
    #     mapsUsed[i].generateMap()
    #
    # e = GameMap("TestMap", seed, width*2, height*2, entryPoints, exitPoints)
    # e.initializeEmptyMap()
    # e.addMap(a.getMap(),0,0,width,height)
    # e.addMap(b.getMap(), width, 0, width, height)
    # e.addMap(c.getMap(), 0, height, width, height)
    # e.addMap(d.getMap(), width, height, width, height)
    # e.printMap()
    # print("Process took: ",str(time.time()-timeKepper)," seconds to complete...")
    # e.exportMap("CombinedMap")

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