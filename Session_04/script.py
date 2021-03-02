import sys

# Task 3 - Sys module exercise
print( "\nTask 3 - Sys module exercise\n" )

def checkArgs( args ):

    if ( len( args ) < 2 or ( len( args ) >= 2 and args[1] != "-ti" ) ):
        print( "Usage: python script.py [-it]{--rm}" )
    elif (  len( args ) == 2 or ( len( args ) > 2 and args[2] != "--rm" ) ):
        print( "Option: {--rm} can be used to remove the container on exit" )

checkArgs( sys.argv )
