# Flower Sin: The Game
# Author: Elliot Schaefer
# A (work in progress) game, that's for sure!

# Imports
import pygame as pg
import random

# Constants
BACKGROUND_COLOR = (0, 0, 0)
BACKGROUND_SIZE = (1000, 1000)

# Custom events
BACKGROUND_CAN_CHANGE_COLOR = pg.event.custom_type()

# Functions
def main():
    
    # Start pygame
    pg.init()

    # Declare Variables
    background_color_change_wait = False

    # Initialize random
    random.seed()

    # Create Main Window
    MainWindow = pg.display.set_mode (BACKGROUND_SIZE)
    
    # Set caption
    pg.display.set_caption ('Flower Sin: The Game')
    
    # Fill screen with BACKGROUND_COLOR
    MainWindow.fill(BACKGROUND_COLOR)
    
    # Begin game loop
    while True:
        
        # Loop through the event cue
        for event in pg.event.get():
        
            # Check for event QUIT
            if event.type == pg.QUIT:
                return

            # Check for Escape key pressed, if so, exit main loop
            elif (event.type == pg.KEYDOWN) and (event.key == pg.K_ESCAPE):
                    return
            # Check if a key has been pressed
            if (event.type == pg.KEYDOWN):
                
                # Check if down key has been pressed
                if event.key == pg.K_DOWN:
                    if background_color_change_wait == False:
                        MainWindow.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                        pg.time.set_timer(BACKGROUND_CAN_CHANGE_COLOR, 1000);
                        background_color_change_wait = True
                    else:
                        print('Wait!')


        
            # Update background_color_change_wait
            if (event.type == BACKGROUND_CAN_CHANGE_COLOR):
                background_color_change_wait = False

        # update display using flip
        pg.display.flip()

        # Increment clock, keep running at 60fps
        pg.time.Clock().tick(60)

# Main, of course
if __name__ == "__main__":
    main()

