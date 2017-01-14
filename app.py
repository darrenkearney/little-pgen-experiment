from worldgenerator import WorldGenerator


def get_input( message = "Provide a number: ", input_type = int ):

    try:

        if input_type == int:
            user_input = int(input(message))
        if input_type == float:
            user_input = float(input(message))

        if user_input:
            return user_input

    except ValueError:

        if input_type == int:
            print("Not an integer. Please enter a number.")
            get_input(message, int)

        if input_type == float:
            print("Not a float. Please enter a number.")
            get_input(message, float)

    

# Set up Controls
x = get_input("What is the length of the area?: [100] ", int)
y = get_input("What is the breath of the area?: [100] ", int)
density = get_input("What is the density of nodes to space? (A percentage)", float)

print("World size: {} by {}.".format( x, y ))

# Run the Generator
gameworld = WorldGenerator(
    WORLD_X = x,
    WORLD_Y = y,
    NODE_DENSITY = density )

gameworld.setup_world_coords()

#gameworld.view_world_coords()

gameworld.generate_world()

gameworld.view_grid()
