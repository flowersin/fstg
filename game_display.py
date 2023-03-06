# A file defining the game display for Flower Sin: The Game
# Author: Elliot Schaefer

import fstg
import pygame as pg

# Constants
DEFAULT_BACKGROUND_COLOR = (100, 100, 100)
DEFAULT_DISPLAY_SIZE = (1000, 1000)
DEFAULT_DISPLAY_CAPTION = 'Flower Sin: The Game'

# Create the disply
class Display:
    
    # Init function
    def __init__(self):
        
        # Create a window
        self.Window = pg.display.set_mode(DEFAULT_DISPLAY_SIZE)
        
        # Set window caption
        pg.display.set_caption(DEFAULT_DISPLAY_CAPTION)

        # fill window with DEFAULT_BACKGROUND_COLOR
        self.Window.fill(DEFAULT_BACKGROUND_COLOR)
    
    def get_display():
        return self.Window

    def random_background_color():
        self.Window.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

