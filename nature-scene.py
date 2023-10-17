# Programmer : Alex Walker
# Description : Draws a nature scene using code

# Import and initialize the pygame library
import pygame
from math import radians
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 800
height = 700

screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")
screen.fill((0, 224, 229))

### PUT YOUR GAME CODE HERE

#Sky
sky_1 = pygame.Rect(0, 0, 900, 900)
pygame.draw.rect(screen, (176, 204, 206), sky_1)

sky_2 = pygame.Rect(0, 0, 700, 900)
pygame.draw.rect(screen, (185, 211, 213), sky_2)

sky_3 = pygame.Rect(0, 0, 500, 900)
pygame.draw.rect(screen, (198, 220, 222), sky_3)

sky_4 = pygame.Rect(0, 0, 250, 900)
pygame.draw.rect(screen, (209, 229, 230), sky_4)

#Far Island

island = pygame.Rect(-120, 399, 330, 55)
pygame.draw.ellipse(screen, (111, 146, 95), island)


#Water
pygame.draw.line(screen, (108, 165, 179), (0, 420), (800, 420), 9 )



water_1 = pygame.Rect(0, 420, 900, 400)
pygame.draw.rect(screen, (108, 165, 179), water_1)

water_2 = pygame.Rect(0, 420, 900, 140)
pygame.draw.rect(screen, (94, 150, 164), water_2)

water_3 = pygame.Rect(0, 420, 900, 40)
pygame.draw.rect(screen, (85, 138, 151), water_3)

#Stone
stone1_point_list = [(310, 400), (330, 480), (300, 680), (500, 500), (310, 400)]
pygame.draw.polygon(screen, (181, 181, 181), stone1_point_list)

stone2_point_list = [(310, 400), (330, 480), (300, 680), (500, 500), (310, 400)]
pygame.draw.polygon(screen, (199, 199, 199), stone2_point_list, 10)

stone3_point_list = [(340, 420), (420, 500), (300, 660), (500, 500), (310, 400)]
pygame.draw.polygon(screen, (159, 159, 159), stone3_point_list)


#Grass
poly3_point_list = [(0,690), (100, 685), (300, 660), (500, 500), (300, 400), (320, 380), (400, 370), (800, 440), (800, 700), (0, 700)]
pygame.draw.polygon(screen, (123, 155, 109), poly3_point_list)

#Sun
pygame.draw.circle(screen, (255, 252, 225), (0, 0), 120)

pygame.draw.circle(screen, (255, 248, 204), (0, 0), 90)

pygame.draw.circle(screen, (250, 243, 193), (0, 0), 70)


#Big Tree

treetrunk_1 = [(390, 400), (340, 410), (400, 400), (460, 410), (420, 290), (460, 210), (390, 120), (360, 140), (400, 220), (360, 300), (340, 410)]
pygame.draw.polygon(screen, (152, 126, 101), treetrunk_1)

treetrunk_2 = [(390, 400), (460, 410), (420, 290), (460, 210), (440, 220), (400, 280)]
pygame.draw.polygon(screen, (137, 113, 90), treetrunk_2)

tree_leaves_1 = [(420, 220), (320, 200), (260, 210), (200, 140), (190, 60), (220, 0), (540, 0), (600, 90), (600, 90), (520, 220), (420, 220)] 
pygame.draw.polygon(screen, (83, 152, 92), tree_leaves_1)

tree_leaves_3 = [(320, 200), (360, 240), (490, 230), (540, 240), (580, 150), (620, 100), (500, 0), (320, 200)]
pygame.draw.polygon(screen, (63, 134, 75), tree_leaves_3)

tree_leaves_2 = [(360, 240), (320, 200), (260, 210), (200, 140), (190, 60), (220, 0), (540, 0), (590, 70), (600, 80), (620, 100), (580, 150), (540, 240), (490, 230)] 
pygame.draw.polygon(screen, (100, 169, 109), tree_leaves_2, 9)

#Birds
pygame.draw.arc(screen, (0,0,0), (200,200,20,30), radians(45), radians(180), 2)
pygame.draw.arc(screen, (0,0,0), (217,195,20,30), radians(45), radians(180), 2)

pygame.draw.arc(screen, (0,0,0), (100,160,20,30), radians(45), radians(180), 2)
pygame.draw.arc(screen, (0,0,0), (117,150,20,30), radians(45), radians(180), 2)









# Uncomment this line to show a grid
#draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
