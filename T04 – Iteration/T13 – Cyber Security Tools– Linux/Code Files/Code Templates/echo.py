import sys

def array_to_string(arr):
    """
    Converts a list of strings into a single concatenated string with spaces between each element.

    Args:
        arr (list of str): A list of strings to be concatenated.

    Returns:
        str: A single string with each element of the list separated by a space.
    """
    result = ""
    
    # Concatenate list elements
    for i in range(len(arr)):
        result += arr[i]
        if i < len(arr) - 1:  # Add a space except for the last element
            result += " "
    
    return result


if __name__ == "__main__":
    # Remove the script name from the list of arguments
    args = sys.argv[1:]

    # If no arguments are provided, print a blank line
    if len(args) == 0:
        print("")
    else:
        # Call `array_to_string()` with the remaining arguments and print the result
        print(array_to_string(args))