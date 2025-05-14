import pygame
import sys

# Initialize pygame
pygame.init()

#setup screen size
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


#colors
black = (0, 0, 0)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black) #fills the screen with black
    pygame.display.update() #updates the display

#Quit game
pygame.quit()
sys.exit()
