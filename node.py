class Node:
    
    def __init__(self, **kwargs):
        self.coords = kwargs.coords
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "Node. Coords: {}".format(self.coords)