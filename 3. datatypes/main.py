# Integer
myint = 7
print(myint)

# Float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Addition
one = 1
two = 2
three = one + two
print(three)

# String
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

# Concat
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
  print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
  print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
  print("Integer: %d" % myint)