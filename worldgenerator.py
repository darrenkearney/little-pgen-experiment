import pprint
class WorldGenerator(object):

    def __init__(self, **kwargs):

        self.NODE_MAX = 100 # default overridden by kwargs
        self.WORLD_X = self.WORLD_Y = 8

        for key, value in kwargs.items():
            setattr(self, key, value)

    def setup_world_coords(self):
        # Set up two dimensional array
        self.world_coords = [ [(x,y) for x in range(0, self.WORLD_X)] for y in range(0, self.WORLD_Y) ]

        print("World Coords are set up")

    def view_world(self):
        pprint.pprint(self.world_coords)
        