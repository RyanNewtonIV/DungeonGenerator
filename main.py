import random
import time
import mapGenerator


if __name__ == '__main__':

    timeKepper = time.time()
    rand = random.Random()
    seed = rand.randint(0, 100000)
    width = 60
    height = 60
    openNess = 0.55
    smoothStep = 5
    minRoomSize = 10
    entryPoints = [[rand.randint(0, width - 1), 0],
                   [rand.randint(0, width - 1), height - 1],
                   [width - 1, rand.randint(0, height - 1)],
                   [0, rand.randint(0, height - 1)]]
    a = mapGenerator.CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints)
    a.getMap()
    a = mapGenerator.GameMap("TestMap", seed, width, height, entryPoints)
    a.getMap()
    print("Process took: ",str(time.time()-timeKepper)," seconds to complete...")