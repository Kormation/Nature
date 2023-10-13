# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 640
height = 360

screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE



# Uncomment this line to show a grid
# draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
