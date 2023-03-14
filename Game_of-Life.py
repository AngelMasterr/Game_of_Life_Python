import pygame
import numpy as np

pygame.init()
# create the screen with its dimensions
width, heigth = 800, 600
screen = pygame.display.set_mode((width, heigth))
# assign a dark gray for the screen background
bg = 25, 25, 25
screen.fill(bg)
# number of cells on the screen
Ncs_x = 32
Ncs_y = 24
# cell size
cell_w = width/Ncs_x
cell_h = heigth/Ncs_y

# estate of the cells. lives = 1; dead = 0;
# create a matrix with the size of the grid
gameState = np.zeros((Ncs_x, Ncs_y))

# keep screen active, crete a inifinite loop
while True:
    # create the cell graphic on the screen
    for y in range(0, Ncs_y):
        for x in range(0, Ncs_x):
            
            # calculate the number of nearest neighbors
            n_neigh = gameState [(x-1) % Ncs_x, (y-1) % Ncs_y] + \
                                [ (x)  % Ncs_x, (y-1) % Ncs_y] + \
                                [(x+1) % Ncs_x, (y-1) % Ncs_y] + \
                                [(x-1) % Ncs_x,  (y)  % Ncs_y] + \
                                [(x+1) % Ncs_x,  (y)  % Ncs_y] + \
                                [(x-1) % Ncs_x, (y+1) % Ncs_y] + \
                                [ (x)  % Ncs_x, (y+1) % Ncs_y] + \
                                [(x+1) % Ncs_x, (y+1) % Ncs_y] 
                                
            # rule 1: one dead cell with exactly three live neighboring cells, "revive" 
            if gameState[x, y] == 0 and n_neigh == 3:
                gameState[x, y] = 1
            
            # rule 2: one live cell with less than two or more than three live neighboring cells, #dies"
            if gameState[x, y] == 1 and n_neigh < 2 or n_neigh > 3:
                gameState[x, y] = 0
            
            #        
            
            # create the polygon each cell to draw
            poly = [(  x    * cell_w,     y   * cell_h),
                    ((x+1)  * cell_w,     y   * cell_h),
                    ((x+1)  * cell_w,   (y+1) * cell_h),
                    (  x    * cell_w,   (y+1) * cell_h)]
            # draw each polygon cell on the screen                                
            pygame.draw.polygon(screen, (128,128,128), poly, width=1)
    # display: show and update the frames in each iteration of the loop    
    pygame.display.flip()
    
