# Task 1 - Alphabet List Comprehensions
print( "\nTask 1 - Alphabet List Comprehensions\n" )

print ( [ x for x in range( 65, 91 ) ] )

l = [ chr( x ) for x in range( ord( 'A' ), ord( 'Z' ) + 1 ) ]

print( l )

l = [ chr( x ) for x in range( 65, 91 ) if x not in [70, 75, 80, 85] ]

print( l )

# F - 70; O - 79 => range ( 71, 79 ) - F and O not included

l = [ chr( x ) for x in range( 65, 91 ) if x not in range( 71, 79, 2 ) ]

print( l )

# Task 2 - Clothes List Comprehension
print( "\nTask 2 - Clothes List Comprehension\n" )

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

l = [ (x, y) for x in colors for y in sizes ]

print( l )

# Task 4 - OS Module Exercise
print( "\nTask 4 - OS Module Exercise\n" )

import os

# Making the directory, if it does not already exist
#    ( from previously running this script )
if not os.path.exists( "os_exercises" ):
    os.mkdir( "os_exercises" )
# Navigating to the directory
os.chdir( "os_exercises" )
# Opening the file to write the input
file = open( "exercise.py", "w" )
file.write( input() )
# Opening the file to append the input
file = open( "exercise.py", "a" )
file.write( input() )
#Reading from the file
file = open( "exercise.py" )
print( file.read() )