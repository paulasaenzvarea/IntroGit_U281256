#My first file tracked by Git
#Author: Paula Sáenz
def greet(name):
    """return a welcome message for the given name"""
    return f"Hello, {name}! Welcome to Git."
def farewell(name):
    """return a goodbye message for the given name"""
    return f"Goodbye, {name}! See you next time."
#This block runs only when the file is executed directly
#not when it is imported as a module from another file
if __name__ == "__main__":
    print(greet('World')) # Call the greet function and print the result
    print(farewell('World')) # Call the farewell function and print the result
    