"""Module showcasing some basic functions."""

def print_hello_world():
    """Function printing hello world."""
    print("Hello World")

def sum_two_numbers(a, b):
    """Function returning the sub of two numbers."""
    return a + b

def my_function_with_args(username, greeting):
    """Function printing a greeting message."""
    print(f"Hello, {username}, From My Function!, I wish you {greeting}")

print_hello_world()
print(sum_two_numbers(10.0, 5))
my_function_with_args("John Doe", "a great year!")
