import sys
import os
import subprocess
import shutil

def main( args ):
    directory = str( args[1] )
    zipping = False
    zip_name = "archive.zip"

    # Move to directory in use
    os.chdir( directory )
    files = list( os.listdir() )

    # Change directory to contain the full path
    directory = str( os.getcwd() )

    print( "\nDirectory to copy from: " + str( os.getcwd() ) )
    print( "\nFiles to be copied: " + str( files ) )

    # Gets destination; if no destination is given, the destination will be the directory in use
    if ( "--todir" in args[2:] and len( args ) >= args.index( "--todir" ) + 2 ):
        destination = str( args[args.index( "--todir" ) + 1] )
    else:
        destination = directory
    
    # Make sure that the destination argument will be treated as a directory
    if ( destination[-1] != "/" ) :
        destination += "/"

    print( "\nFiles will be copied to: " + destination )

    for file in files:
        subprocess.run( ["cp", "-r", file, destination] )
    
    os.chdir( destination )

    # Gets name of the archive; if no name is given, the default name will be archive.zip
    if ( "--zip" in args[2:] ):
        zipping = True
        if ( len( args ) >= args.index( "--zip" ) + 2 ) :
            zip_name = str( args[args.index( "--zip" ) + 1] )
        
        # Make sure that the name contains the ".zip"
        if ( not zip_name.endswith( ".zip" ) ):
            zip_name += ".zip"
        print( "\nZipping to file: " + zip_name )

    if zipping: 
        zip_files = ""
        for file in files: 
            zip_files += file + " "

        #subprocess.run( ["zip", "-r", zip_name, directory] )
        shutil.make_archive( zip_name[:-4], 'zip', directory )

    print( "\nDestination now contains: " + str( os.listdir() ) )

main( sys.argv )