import pprint
import math
from node import Node

class WorldGenerator(object):


    def __init__(self, **kwargs):

        self.NODE_MAX = 100 # default overridden by kwargs
        self.WORLD_X = 8
        self.WORLD_Y = 8
        self.NODE_DENSITY = 32.5

        for key, value in kwargs.items():
            setattr(self, key, value)


    def setup_world_coords(self):

        # Set up two dimensional array
        self.world_coords = [ [(x,y) for x in range(0, self.WORLD_X)] for y in range(0, self.WORLD_Y) ]

        print("World Coords are set up")


    def view_world_coords(self):

        pprint.pprint(self.world_coords)
    

    def get_max_nodes(self):

        self.NODE_DENSITY = 30.2 # percentage as float
    
        area = self.WORLD_X * self.WORLD_Y
    
        node_max = int(area * (self.NODE_DENSITY / 100))
    
        print("Density: {0},\nArea: {1} \nNode max: {2}".format(self.NODE_DENSITY, area, node_max))

        return node_max

        
    def distance_between_two_nodes(self, pointA, pointB):

        x1 = pointA[0]
        y1 = pointA[1]
        x2 = pointB[0]
        y2 = pointB[1]

        return sqrt( ( x2 - x1 ) + ( y2 - y1 ) )

    def make_grid(self):

        # Makes a grid filled with a character

        self.grid = [ ["-" for x in range(0, self.WORLD_X)] for y in range(0, self.WORLD_Y) ]

    def view_grid(self):

        pprint.pprint(self.grid)
    

    def place_nodes(self):

        # This places nodes on new layer abstraction from the coordinates
        # needs to run on an existing grid
        # later I'd like to have different styles of placement for different styles of gameplay and aesthetics

        self.placement_style = "simple"

        if self.placement_style == "simple":
            print("simple math.rand placement")


    def generate_world(self):

        # the 'main' function for generating the world

        self.get_max_nodes()
        self.make_grid()
        self.place_nodes()

        print("world generated")