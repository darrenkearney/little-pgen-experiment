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
WORLD_X = get_input("What is the length of the area?: [100] ", int)
WORLD_Y = get_input("What is the breath of the area?: [100] ", int)
DENSITY = get_input("What is the density of nodes to space? (A percentage)", float)

print("World size: {} by {}.".format( WORLD_X, WORLD_Y ))

# Run the Generator
gen = WorldGenerator(
    WORLD_X = WORLD_X,
    WORLD_Y = WORLD_Y,
    DENSITY = DENSITY )

gen.setup_world_coords()

gen.view_world()

#print("the generators world_x: {}, world_y: {}, density: {}".format(gen.WORLD_X, WORLD_Y, DENSITY))
# Debug code
#print(gen.__dict__)
