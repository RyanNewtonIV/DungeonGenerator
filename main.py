from random import Random
import time
from mapGenerator import GameMap, CaveMap
from randomNameGenerator import RandomNameGenerator



if __name__ == '__main__':

    timeKepper = time.time()
    rand = Random()
    seed = rand.randint(0, 100000)
    width = 60
    height = 60
    openNess = 0.55
    smoothStep = 5
    minRoomSize = 10
    entryPoints = [[rand.randint(1, width - 2), 0],
                   [rand.randint(1, width - 2), height - 1],
                   [width - 1, rand.randint(1, height - 2)],
                   [0, rand.randint(1, height - 2)]]

    a = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints)
    seed = rand.randint(0, 100000)
    b = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints)
    seed = rand.randint(0, 100000)
    c = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints)
    seed = rand.randint(0, 100000)
    d = GameMap("TestMap", seed, width, height, entryPoints)

    e = GameMap("TestMap", seed, width*2, height*2, entryPoints)
    e.initializeEmptyMap()
    e.addMap(a.getMap(),0,0,width,height)
    e.addMap(b.getMap(), width, 0, width, height)
    e.addMap(c.getMap(), 0, height, width, height)
    e.addMap(d.getMap(), width, height, width, height)
    e.printMap()
    print("Process took: ",str(time.time()-timeKepper)," seconds to complete...")
    e.exportMap("CombinedMap")

    r = RandomNameGenerator()
    for i in range(1):
        print(r.returnRandomFirstName("i"))
    for i in range(1):
        print(r.returnRandomLastName())
    for i in range(1):
        print(r.returnRandomFullName("i"))