import pygame
import numpy as np
import time

pygame.init()
# create the screen with its dimensions
width, heigth = 800, 600
screen = pygame.display.set_mode((width, heigth))
# assign a dark gray for the screen background
bg = 25, 25, 25
screen.fill(bg)
# number of cells on the screen
Ncs_x = 40
Ncs_y = 30
# cell size
cell_w = width/Ncs_x
cell_h = heigth/Ncs_y

# estate of the cells. lives = 1; dead = 0;
# create a matrix with the size of the grid
gameState = np.zeros((Ncs_x, Ncs_y))

# key or mouse button variables
pauseExect = False


# keep screen active, crete a inifinite loop
while True:
    # create copy of matriz to not alter the results of the entire loop
    new_gameState = np.copy(gameState)       
    # clear the screen so that previus results do not overlap
    screen.fill(bg)    
    # generate a small delay for the system to take a breath and we can see the change of cells
    time.sleep(0.1)
    
    # check if a key or mouse button is pressed
    ev = pygame.event.get()   
    for event in ev:
         # swap the variable "pauseExect" between False and True
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        # check which mouse button is pressed
        mouse_click = pygame.mouse.get_pressed()
        # if left mouse buton is pressed the cell become to 1, "live"
        if any(mouse_click) == True:
            pos_x, pos_y = pygame.mouse.get_pos()
            cel_x, cel_y = int(np.floor(pos_x/cell_w)), int(np.floor(pos_y/cell_h)) 
            if mouse_click[0] == True:
                new_gameState[cel_x, cel_y] = 1
            # if right mouse buton is pressed the cell become to 0, "dead"
            elif mouse_click[2] == True:
                new_gameState[cel_x, cel_y] = 0 
            elif mouse_click[1] == True:
                new_gameState = np.zeros((Ncs_x, Ncs_y))   
    
    # create the cell graphic on the screen
    for y in range(0, Ncs_y):
        for x in range(0, Ncs_x):
            
            # control the execution of the game
            if not pauseExect:
            
                # calculate the number of nearest neighbors
                n_neigh = gameState [(x-1) % Ncs_x, (y-1) % Ncs_y] + \
                        gameState [ (x)  % Ncs_x, (y-1) % Ncs_y] + \
                        gameState [(x+1) % Ncs_x, (y-1) % Ncs_y] + \
                        gameState [(x-1) % Ncs_x,  (y)  % Ncs_y] + \
                        gameState [(x+1) % Ncs_x,  (y)  % Ncs_y] + \
                        gameState [(x-1) % Ncs_x, (y+1) % Ncs_y] + \
                        gameState [ (x)  % Ncs_x, (y+1) % Ncs_y] + \
                        gameState [(x+1) % Ncs_x, (y+1) % Ncs_y] 
                                    
                # rule 1: one dead cell with exactly three live neighboring cells, "revive" 
                if gameState[x, y] == 0 and n_neigh == 3:
                    new_gameState[x, y] = 1
                
                # rule 2: one live cell with less than two or more than three live neighboring cells, #dies"
                if gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_gameState[x, y] = 0            
           
            # create the polygon each cell to draw
            poly = [(  x    * cell_w,     y   * cell_h),
                    ((x+1)  * cell_w,     y   * cell_h),
                    ((x+1)  * cell_w,   (y+1) * cell_h),
                    (  x    * cell_w,   (y+1) * cell_h)]
            
            # draw each polygon cell on the screen for each x, y   
            if new_gameState[x, y] == 0:                           
                pygame.draw.polygon(screen, (128,128,128), poly, width=1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, width=0)
    
    # we update the state of the game
    gameState = np.copy(new_gameState)
                
    # display: show and update the frames in each iteration of the loop    
    pygame.display.flip()
    
