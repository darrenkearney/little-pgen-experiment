#from generator import Generator


def get_int_input(message="Provide a number: "):

    try:
        user_input = int(input(message))
        return user_input 
    except ValueError:
        print("Not an integer. Please enter a number.")
        get_int_input(message)

NODE_MAX = get_int_input("How many nodes (rooms) do you want to generate?: [100] ")

print("Node max: {}".format( NODE_MAX ))

# Run the Generator
#gen = new Generator( { node_max: NODE_MAX } )
