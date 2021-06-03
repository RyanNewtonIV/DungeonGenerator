import random
import time
from mapGenerator import GameMap, CaveMap



if __name__ == '__main__':

    timeKepper = time.time()
    rand = random.Random()
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
    a.getMap()
    b = GameMap("TestMap", seed, width, height, entryPoints)
    b.getMap()
    print("Process took: ",str(time.time()-timeKepper)," seconds to complete...")