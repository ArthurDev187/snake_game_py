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
snake_pos = [100, 50] # Initial position (y, x) head
snake_body = [[100, 50], [80, 50], [60, 50]] # Initial body (3 blocks)
direction = 'RIGHT'

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'



    # Move the head
    if direction == 'RIGHT':
        snake_pos[0] += block_size
    elif direction == 'LEFT':
        snake_pos[0] -= block_size
    elif direction == 'UP':
        snake_pos[1] -= block_size
    elif direction == 'down':
        snake_pos[1] += block_size


    # add new head to the body
    snake_body.insert(0, list(snake_pos))
    # remove the last block (tail) to simulate the movement
    snake_body.pop()

    screen.fill(black) #fills the screen with black

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], block_size, block_size))


    pygame.display.update() #updates the display
    clock.tick(10) # 10 frames per second

#Quit game
pygame.quit()
sys.exit()
