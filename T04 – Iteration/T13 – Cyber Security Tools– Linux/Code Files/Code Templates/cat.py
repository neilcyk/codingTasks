#!/usr/bin/python3
import os
import sys

"""
This script processes input either from standard input (stdin) or from a
specified file. Reads lines from stdin or a file and prints them to standard
output (stdout).

Usage:
    - If no arguments are provided, reads from stdin.
    - If a filename is provided as a command-line argument, reads from that
      file.

Modules:
    sys: Provides access to command-line arguments and standard input/output
    streams.
"""
import sys

def std_in():
    """
    This function reads input from standard input (stdin) and prints each line
    to standard output (stdout). This simulates the behavior of the 'cat' command.
    """
    # TODO: Implement the function to read from stdin and print each line.
    # Read from stdin and print each line.
    with open("something.txt", "r") as file:
    # Loop over each line from standard input (stdin)
        for line in file:
            # Print each line to standard output (stdout)
            print(line, end='')
# Call the function
std_in()

def infile(file):
    
    if file:
        # Check if the file exists before trying to read it
        if os.path.exists(file):
            with open(file, 'r') as f:
                # Read the file line by line and print its contents
                for line in f:
                    print(line, end='')  # Print each line without extra newline
        else:
            print(f"Error: The file '{file}' was not found.")
    else:
        # If no file argument, read from stdin
        print("Reading from standard input (Ctrl+D to end input):")
        # Use a while loop to continuously read from stdin until EOF
        while True:
            try:
                line = input()  # Read a line from stdin
                print(line)     # Print the line to stdout
            except EOFError:
                break  # End the loop when EOF (Ctrl+D) is reached

# Determine whether to read from stdin or from a file based on
# command-line arguments. The length of sys.argv is checked to
# decide the source of input. sys.argv[0] is the name of this
# script, so we check for additional arguments (i.e., len(sys.argv) > 1).

if __name__ == "__main__":
    # TODO: Implement the logic to decide whether to call infile() or std_in()
    # based on the number of command-line arguments.
    if len(sys.argv) > 1:
        # If more than one argument is provided, use the second argument as the file path
        infile(sys.argv[1])  # Call infile() with the file path from the command-line argument
    else:
        # Otherwise, read from standard input
        std_in()  # Call std_in() to read from standard input
    # Check the number of command-line arguments
    # If more than one argument is provided, use the second argument as the file path.
    # Otherwise, read from standard input.
    pass
