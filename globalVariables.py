# global variables.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# local variables.
x = "awesome"

def myfunc():
  x = "fantastic" # local variable.
  print("Python is " + x)

myfunc()

print("Python is " + x)

# global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# change the value of a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)