import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
yellow = (255,255,0)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('')

clock = pygame.time.Clock()

block_size = 20
FPS = 30

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):

    for XY in snakelist:
        if XY[1]<display_height/3:
            pygame.draw.rect(gameDisplay, green, [XY[0], XY[1], block_size, block_size])
        elif XY[1] > display_height/3 and XY[1]< 2*display_height/3:
            pygame.draw.rect(gameDisplay, black, [XY[0], XY[1], block_size, block_size])
        else:
            tracker = int((time.time() * 1000) % 500)
            if tracker < 250:
                pygame.draw.rect(gameDisplay, black, [XY[0], XY[1], block_size, block_size])
            else:
                pygame.draw.rect(gameDisplay, green, [XY[0], XY[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0

    randenemyX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
    randenemyY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        pygame.draw.rect(gameDisplay, yellow, [randenemyX, randenemyY, AppleThickness, AppleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        ##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        ##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                randenemyX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randenemyY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0

                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                randenemyX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randenemyY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0

                snakeLength += 1

        if lead_x > randenemyX and lead_x < randenemyX + AppleThickness or lead_x + block_size > randenemyX and lead_x + block_size < randenemyX + AppleThickness:

            if lead_y > randenemyY and lead_y < randenemyY + AppleThickness:

                randenemyX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randenemyY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                del snakeList[0]
                snakeLength-=1

            elif lead_y + block_size > randenemyY and lead_y + block_size < randenemyY + AppleThickness:

                randenemyX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randenemyY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                del snakeList[0]
                snakeLength-=1

        if(snakeLength==0):
            gameOver=True


        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()














