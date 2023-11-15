import sys

import pygame

class Game:
    def __init__(self):

        pygame.init() # initializing pygame

        pygame.display.set_caption('Ninja Game') # setting the window name
        self.screen = pygame.display.set_mode((640,480)) # setting display height and width

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))

        self.img_pos = [160,260]
        self.movement = [False, False]

    def run(self):
        while True: # infinite loop
            self.screen.fill((14, 219, 248))


            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 2
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get(): #adding the feature of quiting the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False

            pygame.display.update() # updating the window
            self.clock.tick(60) # 60 because of 60hz

Game().run()