import pygame as pg
import sys
from settings import *  # Import game settings (e.g., resolution, FPS)
from map import *       # Import the map-related functionality
from player import *    # Import player-related functionality
from raycasting import *  # Import raycasting logic for rendering 3D projections
from object_renderer import *  # Import object rendering (e.g., textures, backgrounds)
from sprite_object import *  # Import sprite handling for 2D and 3D objects
from object_handler import *  # Import logic for handling in-game objects
from weapon import *  # Import weapon-related logic
from sound import *  # Import sound and music functionalities
from pathfinding import *  # Import pathfinding logic for AI or navigation

# Main Game Class
class Game:
    def __init__(self):
        # Initialize Pygame and configure basic settings
        pg.init()
        pg.mouse.set_visible(False)  # Hide the mouse cursor
        self.screen = pg.display.set_mode(RES)  # Set the game resolution
        pg.event.set_grab(True)  # Confine the mouse to the game window
        self.clock = pg.time.Clock()  # Initialize a clock for managing FPS
        self.delta_time = 1  # Time between frames
        self.global_trigger = False  # A trigger for global events
        self.global_event = pg.USEREVENT + 0  # Define a custom Pygame event
        pg.time.set_timer(self.global_event, 40)  # Trigger the event every 40ms
        self.new_game()  # Initialize a new game instance

    def new_game(self):
        # Initialize all game components
        self.map = Map(self)  # Load the game map
        self.player = Player(self)  # Initialize the player
        self.object_renderer = ObjectRenderer(self)  # Manage rendering objects
        self.raycasting = RayCasting(self)  # Handle raycasting for visuals
        self.object_handler = ObjectHandler(self)  # Manage game objects
        self.weapon = Weapon(self)  # Initialize player weapon
        self.sound = Sound(self)  # Initialize sound effects
        self.pathfinding = PathFinding(self)  # Initialize pathfinding (e.g., AI navigation)
        pg.mixer.music.play(-1)  # Start background music (loop infinitely)

    def update(self):
        # Update all game components each frame
        self.player.update()  # Update player position and actions
        self.raycasting.update()  # Update raycasting for visuals
        self.object_handler.update()  # Update object interactions
        self.weapon.update()  # Update weapon state
        pg.display.flip()  # Update the full display surface to the screen
        self.delta_time = self.clock.tick(FPS)  # Control frame rate and calculate delta time
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')  # Show FPS in the window title

    def draw(self):
        # Draw all visual components of the game
        # self.screen.fill('black')  # Optional: Fill the screen with a background color
        self.object_renderer.draw()  # Render objects (e.g., walls, environment)
        self.weapon.draw()  # Render the weapon
        # self.map.draw()  # Optional: Debug map visualization
        # self.player.draw()  # Optional: Debug player visualization

    def check_events(self):
        # Handle user input and game events
        self.global_trigger = False  # Reset global event trigger
        for event in pg.event.get():  # Loop through all active events
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # Exit the game on Quit or Escape key press
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                # Trigger global event logic
                self.global_trigger = True
            self.player.single_fire_event(event)  # Handle single fire actions (e.g., shooting)

    def run(self):
        # Main game loop
        while True:
            self.check_events()  # Process events
            self.update()  # Update game logic
            self.draw()  # Render visuals


# Entry point of the program
if __name__ == '__main__':
    game = Game()  # Create a Game instance
    game.run()  # Start the game loop
