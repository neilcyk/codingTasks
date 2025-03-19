import sys

def match(source, needle):
    """
    Searches for a specified 'needle' string within a list of 'source' strings.

    Args:
        source (iterable): An iterable of strings to be searched.
        needle (str): The string to search for within each string in 'source'.

    Prints:
        The lines from 'source' that contain 'needle'.

    Example:
        If 'source' is ['line1', 'needle line2', 'line3'] and 'needle' is 'needle', the function will print 'needle line2'.
    """
    # loop each line in 'source'
    for line in source:
        if needle in line:  # Check if the 'needle' is found in the current line
            print(line, end='')  # Print the matching line

if __name__ == "__main__":
    """
    Main execution of the script. Determines whether to read input from stdin or from a specified file based on command-line arguments.

    - If exactly one argument is provided (the needle), reads from stdin.
    - If two arguments are provided (the needle and filename), reads from the specified file.
    """
    # Check the number of command-line arguments
    if len(sys.argv) == 2:
        # If only the 'needle' is provided, read from stdin
        print("Enter text (Ctrl+D to quit):")
        lines = []
        while True:
            try:
                line = input()  # Read input line by line
                lines.append(line + "\n")  # Store lines for searching
            except EOFError:
                break  # Stop reading on EOF
        match(lines, sys.argv[1])
    
    elif len(sys.argv) == 3:
        # Read the file if 'needle' and 'filename' are provided
        filename = sys.argv[2]
        lines = []
        
        # Read file content
        file_found = False
        for _ in range(1):  # Simulating 'if' condition within a loop
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()  # Read all lines from the file
                file_found = True
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
        
        if file_found:
            match(lines, sys.argv[1])  # Call match() with file content

    else:
        print("Usage: python script.py needle [filename]")