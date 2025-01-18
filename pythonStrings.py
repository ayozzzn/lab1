# display a string.
print("Hello")
print('Hello')

# quotes inside quotes.
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# assign string to a variable.
a = "Hello"
print(a)

# multiline strings.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # three double quotes.
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' # three single quotes.
print(a)

# strings are arrays.
a = "Hello, World!"
print(a[1])

# looping through a string.
for x in "banana":
  print(x)

  # string length.
a = "Hello, World!"
print(len(a))

# check string.
txt = "The best things in life are free!"
print("free" in txt)

# use it in an 'if' statement.
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# check if NOT.
txt = "The best things in life are free!"
print("expensive" not in txt)

# use it in an 'if' statement.
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

