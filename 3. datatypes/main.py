"""Module exercising different variable datatypes."""

# Integer
MY_INT = 7
print(MY_INT)

# Float
MY_FLOAT = 7.0
print(MY_FLOAT)
MY_FLOAT = float(7)
print(MY_FLOAT)

# Addition
ONE = 1
TWO = 2
THREE = ONE + TWO
print(THREE)

# String
MY_STRING = 'hello'
print(MY_STRING)
MY_STRING = "hello"
print(MY_STRING)
MY_STRING = "Don't worry about apostrophes"
print(MY_STRING)

# Concat
HELLO = "hello"
WORLD = "world"
HELLO_WORLD = HELLO + " " + WORLD
print(HELLO_WORLD)

# change this code
MY_STRING = "hello"
MY_FLOAT = 10.0
MY_INT = 20

# testing code
if MY_STRING == "hello":
    print(f"String: {MY_STRING}")
if isinstance(MY_FLOAT, float) and MY_FLOAT == 10.0:
    print(f"Float: {MY_FLOAT}")
if isinstance(MY_INT, int) and MY_INT == 20:
    print(f"Integer: {MY_INT}")
