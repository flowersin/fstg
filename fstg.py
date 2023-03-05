# Flower Sin: The Game
# Author: Elliot Schaefer
# A (work in progress) game, that's for sure!

# Imports
import pygame as pg

# Constants
BACKGROUND_COLOR = (0, 0, 0)
BACKGROUND_SIZE =(1000, 1000)

# Functions
def main():
    # Create Main Window
    MainWindow = pg.display.set_mode(BACKGROUND_SIZE)
    
    # Set caption
    pg.display.set_caption('Flower Sin: The Game')
    
    # Fill screen with BACKGROUND_COLOR
    MainWindow.fill(BACKGROUND_COLOR)

    # update display using flip
    pg.display.flip()

    # Begin game loop while running is true
    running = True
    while running:
        
        # Loop through the event cue
        for event in pg.event.get():
        
            # Check for event QUIT
            if event.type == pg.QUIT:
                running = False
    
# Main, of course
if __name__ == "__main__":
    main()

