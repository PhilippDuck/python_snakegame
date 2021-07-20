"""

ToDo´s:
- highscores 

"""


import pygame
import time
import random

class Game:
    
    def __init__(self):
        pygame.init()
        self.width = 550
        self.height = 550
        self.blocksize = self.width/11
        self.run = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self. height))
        pygame.display.set_caption("PYTHON!")

    def show_Background(self):
        self.window.fill((50, 77, 120))
        for line in range(11):
            y = line*self.blocksize
            for block in range(11):
                pygame.draw.rect(self.window, (111, 137, 179), (block*self.blocksize, y, self.blocksize, self.blocksize), 1)


class Menue:

    def __init__(self, window):
        self.window = window
        self.color = (104, 120, 146)
    
    def showMenue(self):
        menueText = font.render("GAME OVER - PRESS SPACE TO RESTART", True, (255,255,255))
        pygame.draw.rect(self.window, self.color, (game.width/2 - menueText.get_width()/2 - 5, game.height/2 - menueText.get_height()/2 - 5, menueText.get_width() + 10, menueText.get_height() + 10))
        self.window.blit(menueText, (game.width/2 - menueText.get_width()/2, game.height/2 - menueText.get_height()/2))

    def showStartMenue(self):
        menueText = font.render("PYTHON! - PRESS SPACE TO START", True, (255,255,255))
        pygame.draw.rect(self.window, self.color, (game.width/2 - menueText.get_width()/2 - 5, game.height/2 - menueText.get_height()/2 - 5, menueText.get_width() + 10, menueText.get_height() + 10))
        self.window.blit(menueText, (game.width/2 - menueText.get_width()/2, game.height/2 - menueText.get_height()/2))

    def showPauseMenue(self):
        menueText = font.render("PAUSE - PRESS SPACE TO RESUME", True, (255,255,255))
        pygame.draw.rect(self.window, self.color, (game.width/2 - menueText.get_width()/2 - 5, game.height/2 - menueText.get_height()/2 - 5, menueText.get_width() + 10, menueText.get_height() + 10))
        self.window.blit(menueText, (game.width/2 - menueText.get_width()/2, game.height/2 - menueText.get_height()/2))
        

class Snake:

    def __init__(self, window, blocksize):
        self.window = window
        self.blocksize = blocksize
        self.speed = 0.8
        self.block = 5
        self.line = 5
        self.direction = 4       # 1=Up 2=Right 3=Down 4=Left
        self.lastMovedTime = time.time()
        self.tailLenght = 0
        self.tail = []
        self.color = (0, 242, 161)

    def show(self):
        pygame.draw.rect(self.window, self.color, (self.block*self.blocksize, self.line*self.blocksize,
            self.blocksize, self.blocksize))

        removeitems = self.tail.__len__() - self.tailLenght
        del self.tail[:removeitems]
        if self.tail.__len__() >= 1:
            for blocks in self.tail:
                pygame.draw.rect(self.window, (0, 242, 117), (blocks[0]*self.blocksize, blocks[1]*self.blocksize,
                    self.blocksize, self.blocksize))
        self.showPoints()

    def move(self):
        if (time.time() - self.lastMovedTime) >= self.speed:
            self.tail.append((self.block, self.line))

            if self.direction == 1:
                if self.line <= 0:
                    self.line = 10
                else:
                    self.line -= 1

            if self.direction == 2:
                if self.block >= 10:
                    self.block = 0
                else:
                    self.block += 1

            if self.direction == 3:
                if self.line >= 10:
                    self.line = 0
                else:
                    self.line += 1

            if self.direction == 4:
                if self.block <= 0:
                    self.block = 10
                else:
                    self.block -= 1
            self.lastMovedTime = time.time()

    def checkKollision(self):
        if (self.block, self.line) in self.tail:
            print("AUA!")
            return True
        else:
            False
            
    def checkSnack(self, fruit):
        if self.block == fruit.block and self.line == fruit.line:
            self.tailLenght += 1
            #print(self.tail)
            if self.speed > 0.04:
                self.speed -= 0.02
            return True
        else:
            return False
    
    def showPoints(self):
        pointText = font.render(str(self.tailLenght), True, (255,255,255))
        game.window.blit(pointText,(20,15))


    
class Fruit:

    def __init__(self, window, blocksize, poslist):
        self.window = window
        self.blocksize = blocksize
        self.color = (242, 91, 53)
        self.block = 0
        self.line = 0
        self.getPos(poslist)

    def __del__(self):
        print("fruit snacked!")
    
    def getPos(self, poslist):
        position = (random.randint(0,10),random.randint(0,10))
        print(snake.tail)
        while position in poslist:
            print("Frucht in Schlange, erneut spawnen.")
            position = (random.randint(0,10),random.randint(0,10))
        self.block = position[0]
        self.line = position[1]
        

    def show(self):
        pygame.draw.rect(self.window, self.color, (self.block*self.blocksize, self.line*self.blocksize,
            self.blocksize, self.blocksize))

pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 36)

game = Game()
snake = Snake(game.window, game.blocksize)
fruit = Fruit(game.window, game.blocksize, snake.tail)
menue = True
menueIsOpen = False
menueCounter = 0

while game.run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        menue = False
        menueIsOpen = False


    if not menue:
        if keys[pygame.K_UP]:
            snake.direction = 1
        if keys[pygame.K_RIGHT]:
            snake.direction = 2
        if keys[pygame.K_DOWN]:
            snake.direction = 3
        if keys[pygame.K_LEFT]:
            snake.direction = 4
        if keys[pygame.K_ESCAPE]:
            menue = True
            menueIsOpen = True
            menue = Menue(game.window)
            menue.showPauseMenue()    

        game.show_Background()
        fruit.show()
        snake.move()

        if snake.checkKollision():
            menue = True
            del snake
            snake = Snake(game.window, game.blocksize)
        if snake.checkSnack(fruit):
            del fruit
            fruit = Fruit(game.window, game.blocksize, snake.tail)

        snake.show()

        if keys[pygame.K_ESCAPE]:
            menue = True
            menueIsOpen = True
            menue = Menue(game.window)
            menue.showPauseMenue()  

    if menue and not menueIsOpen:
        game.show_Background()

        menue = Menue(game.window)
        menueIsOpen = True
        if menueCounter <= 0:
            menue.showStartMenue()
        else:
            menue.showMenue()
        menueCounter += 1

    pygame.display.flip()
    game.clock.tick(60)

pygame.quit()