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
stone1_point_list = [(310, 400), (330, 480), (300, 680), (500, 500), (310, 400)]
pygame.draw.polygon(screen, (181, 181, 181), stone1_point_list)

stone2_point_list = [(340, 420), (420, 500), (300, 660), (500, 500), (310, 400)]
pygame.draw.polygon(screen, (159, 159, 159), stone2_point_list)

#Grass
poly3_point_list = [(0,690), (100, 685), (300, 660), (500, 500), (300, 400), (320, 380), (400, 370), (800, 440), (800, 700), (0, 700)]
pygame.draw.polygon(screen, (123, 155, 109), poly3_point_list)

#Big Tree
treetrunk_point_list = [(390, 400), (340, 410), (400, 400), (460, 410), (420, 290), (460, 210), (390, 120), (360, 140), (400, 220), (360, 300), (340, 410)]
pygame.draw.polygon(screen, (152, 126, 101), treetrunk_point_list)

tree_leaves_1 = [(420, 220), (320, 200), (260, 210), (200, 140), (190, 60), (220, 0), (540, 0), (600, 90), (600, 90), (520, 220), (420, 220)] 
pygame.draw.polygon(screen, (83, 152, 92), tree_leaves_1)






# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
