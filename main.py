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
green = (0, 255, 0)

# Clock (to control the frame rate)
clock = pygame.time.Clock()

# Snake settings
block_size = 20
snake_pos = [100, 50] # Initial position (y, x)
snake_body = [[100, 50], [80, 50], [60, 50]] # Initial body (3 blocks)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black) #fills the screen with black

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], block_size, block_size))


    pygame.display.update() #updates the display
    clock.tick(10) # 10 frames per second

#Quit game
pygame.quit()
sys.exit()
