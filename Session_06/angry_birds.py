import random
import sys

def spacer():
    print( "\n***\n" )

def generate_coordinates( min, max ):
    return ( random.randint( min, max ), random.randint( min, max ) )

class Bird:
    directions = ["up", "right", "down", "left"]
    directions_signs = ["^", ">", "v", "<"]

    def __init__( self, pos_x, pos_y ):
        # Coordinates on an X, Y Axis
        self.current_position = [pos_x, pos_y]
        self.direction = Bird.directions[0]

    def move( self ):
        direction_index = Bird.directions.index( self.direction )

        # Determines whether the move will happen on the X (0) or Y (1) axis
        axis = direction_index % 2
        # Determines whether the value on the axis has to increase or decrease
        if direction_index in [0, 3]:
            self.current_position[axis] -= 1
        else:
            self.current_position[axis] += 1

        print( "Moved to:", self.current_position )

    def change_direction( self, direction ):
        direction_index = Bird.directions.index( self.direction )

        if direction == "left":
            direction_index = ( direction_index - 1 ) % 4
        elif direction == "right":
            direction_index = ( direction_index + 1 ) % 4
        else:
            print( "Invalid Direction." )

        self.direction = Bird.directions[direction_index]
        print( "Turning", direction )
        print( "Facing:", self.direction, Bird.directions_signs[direction_index] )

    def on_win( self ):
        print( "Bird: I've hit the Pig !" )

    def on_lose( self ):
        print( "Bird: Oh no, I missed !" )

class Pig:
    def __init__( self, pos_x = 0, pos_y = 0 ):
        self.position = [pos_x, pos_y]
    
    def on_win( self ):
        print( "Pig: Ha-ha, you missed !" )

    def on_lose( self ):
        print( "Pig: Ugh, I've been hit !" )

class Board:
    def __init__( self, size):
        self.size = size
        self.board = [ [ "*" for j in range( size ) ] for i in range( size ) ]

    def initialize( self, pig_coords, bird_coords ):
        spacer()
        self.pig = Pig( pig_coords[0], pig_coords[1] )
        self.bird = Bird( bird_coords[0], bird_coords[1] )

        self.board[pig_coords[0]][pig_coords[1]] = "P"
        self.board[bird_coords[0]][bird_coords[1]] = "B"

        print( f"Initializing Board with the Pig @({ self.pig.position[0] }, { self.pig.position[1] })" +
               f" and the Bird @({ self.bird.current_position[0] }, { self.bird.current_position[1] })." )
    
    def display( self ):
        spacer()
        for i in range( self.size ):
            for j in range(self.size):
                print( self.board[i][j], end=" " )
            print()

    def run( self ):
        # Generating the coordinates of the Pig
        pig_coords = generate_coordinates( 0, self.size - 1 )
        
        # Generating the coordinates of the Bird
        bird_coords = generate_coordinates( 0, self.size - 1 )

        # Making sure the Pig and the Bird have different coordinates.
        while pig_coords == bird_coords:
            bird_coords = generate_coordinates( 0, self.size - 1 )
        
        self.initialize( pig_coords, bird_coords )
        self.display()

class Workspace:
    def __init__( self ):
        self.instruction_number = 0
        self.instruction_list = []

    def display( self ):
        spacer()
        print( "Objective: Help the Bird ( B ) to hit the Pig ( P ) by providing the proper instructions." )
        print( "Options: Move Forward ( 'f' ), Turn Left ( 'l' ), Turn Right ( 'r' )." )
        print( "When you have finished giving instructions to the Bird, press 'q'. " )
        print( "Note: By default, the Bird is facing 'up'." )
    
    # Creates a list of instructions from the input recieved from the User
    def take_instructions( self ):
        while True:
            self.instruction_number += 1
            instruction = input( f"Instruction No.{ self.instruction_number }: " )
            
            if instruction == "f":
                self.instruction_list.append( "f" )
            elif instruction == "l":
                self.instruction_list.append( "l" )
            elif instruction == "r":
                self.instruction_list.append( "r" )
            elif instruction == "q":
                print( "Quitting." )
                spacer()
                break
            else:
                print( "Invalid instruction... Try again !" )
                self.instruction_number -= 1
    
        

class Game:
    def __init__( self, board_size ):
        self.board = Board( board_size )
        self.workspace = Workspace()

    def run( self ):
        # Creates the Board
        self.board.run()

        # Prints the instructions
        self.workspace.display()

        # Takes the user input
        self.workspace.take_instructions()

        # Executes the commands
        for instruction in self.workspace.instruction_list:
            if instruction == "f":
                self.board.bird.move()
            elif instruction == "l":
                self.board.bird.change_direction( "left" )
            else:
                self.board.bird.change_direction( "right" )

        self.check_win()

    def check_win( self ):
        if self.board.pig.position == self.board.bird.current_position:
            print( "You Won !" )
            self.board.pig.on_lose()
            self.board.bird.on_win()
        else:
            print( "You Lost !" )
            self.board.pig.on_win()
            self.board.bird.on_lose()
        spacer()

game = Game( int( sys.argv[1] ) )
game.run()
