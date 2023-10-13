# Programmer : Alex Walker
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 800
height = 700

screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")
screen.fill((214, 224, 229))

### PUT YOUR GAME CODE HERE

#Stone
poly2_point_list = [(310, 400), (330, 480), (310, 680)]
pygame.draw.polygon(screen, (181, 181, 181), poly2_point_list, 6)

#Grass
poly1_point_list = [(0,690), (100, 685), (300, 660), (500, 500), (300, 400), (320, 380), (400, 370), (800, 440), (800, 700), (0, 700)]
pygame.draw.polygon(screen, (123, 155, 109), poly1_point_list)



# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
