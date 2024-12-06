import pygame as pg

# Define the mini-map layout using a 2D grid
# `1` - Represents walls or solid objects
# `3`, `4`, `5` - Represent other objects (e.g., special zones, enemies, or features)
# `_` - Represents empty space (False)
_ = False  # Alias for readability, represents empty space
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1, 3, _, _, 3, 1, 1, 1],
    [1, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, 3, 4, _, 4, 3, _, 1],
    [1, _, _, 5, _, _, _, _, _, _, 3, _, 3, _, _, 1],
    [1, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 4, _, _, _, _, _, _, 4, _, _, 4, _, _, _, 1],
    [1, 1, 3, 3, _, _, 3, 3, 1, 3, 3, 1, 3, 1, 1, 1],
    [1, 1, 1, 3, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 4, _, _, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, 5, _, _, _, 5, _, _, _, 5, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

# Map Class
class Map:
    def __init__(self, game):
        """Initialize the Map class with game reference and load the mini-map."""
        self.game = game  # Reference to the main game object
        self.mini_map = mini_map  # Mini-map layout
        self.world_map = {}  # Dictionary to store world coordinates and their values
        self.rows = len(self.mini_map)  # Number of rows in the mini-map
        self.cols = len(self.mini_map[0])  # Number of columns in the mini-map
        self.get_map()  # Convert mini-map to world coordinates

    def get_map(self):
        """Convert the 2D mini-map into a dictionary of world coordinates."""
        for j, row in enumerate(self.mini_map):  # Enumerate rows
            for i, value in enumerate(row):  # Enumerate columns
                if value:  # Only store non-empty cells
                    self.world_map[(i, j)] = value  # Map (x, y) -> value

    def draw(self):
        """Draw the mini-map onto the screen for debugging."""
        for pos in self.world_map:  # Iterate through all coordinates
            # Draw a rectangle representing each non-empty cell
            pg.draw.rect(
                self.game.screen,  # Surface to draw on
                'darkgray',  # Rectangle color
                (pos[0] * 100, pos[1] * 100, 100, 100),  # Position and size
                2,  # Outline thickness
            )
