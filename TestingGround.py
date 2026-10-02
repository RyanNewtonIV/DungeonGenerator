from random import Random
import pygame
from mapGenerator import GameMap, CaveMap


if __name__ == '__main__':

    rand = Random()
    seed = rand.randint(0, 100000)
    width = 200
    height = 150
    openNess = .4
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

    # Map Creation
    a = CaveMap("TestMap", seed, width, height, 4, 3, openNess, smoothStep, minRoomSize, entryPoints, exitPoints)
    a.generateMap()
    a.printMap(a.getMap())
    fillMap = a.generateFillMap()
    a.printMapValues(fillMap)
    print(a)
    print(a.entryPoints[0])
    print(a.exitPoints[0])

    pygame.init()

    pygame.display.set_caption('Hero Arena')
    screenWidth = 800
    screenHeight = 600

    screen = pygame.display.set_mode((screenWidth,screenHeight))

    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 255, 0)
    GREEN = (0, 255, 0)
    TEAL = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (255, 0, 255)

    scalingValue = 4

    run = True
    mapToPrint = a.getMap()
    for j in range(len(mapToPrint[0])):
        for i in range(len(mapToPrint)):
            if mapToPrint[i][j] == 0:
                pygame.draw.rect(screen,BLUE,(i*scalingValue,j*scalingValue,1*scalingValue,1*scalingValue))
    while run:

        #screen.fill((0, 0, 0))

        #pygame.draw.rect(screen, BLUE, (200, 150, 100, 50),15)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
