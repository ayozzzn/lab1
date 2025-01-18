# converts the first character to upper case.
x = "hello, World!"
uppercase = x.capitalize()
print(uppercase) # Hello, world!

# converts string into lower case.
x = "Hello, World!"
lowercase = x.casefold()
print(lowercase) # hello, world!

# returns a centered string.
x = "hello!"
centered = x.center(10, '-')
print(centered) # --hello!--  

# returns the number of times a specified value occurs in a string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) # 2

# returns an encoded version of the string.
txt = "My name is Ståle"
x = txt.encode()
print(x) # b'My name is St\xc3\xa5le'

# returns true if the string ends with the specified value.
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) # True

# sets the tab size of the string.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x) # H e l l o

# searches the string for a specified value and returns the position of where it was found.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # 7

# formats specified values in a string.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) # For only 49.00 dollars!

# searches the string for a specified value and returns the position of where it was found.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) # 7

# returns True if all characters in the string are alphanumeric.
txt = "Company12"
x = txt.isalnum()
print(x) # True

# returns True if all characters in the string are in the alphabet.
txt = "CompanyX"
x = txt.isalpha()
print(x) # True

# returns True if all characters in the string are digits.
txt = "50800"
x = txt.isdigit()
print(x) # True

# returns True if all characters in the string are lower case.
txt = "hello world!"
x = txt.islower()
print(x) # True

# returns True if all characters in the string are upper case.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # True

# converts a string into lower case.
txt = "Hello my FRIENDS!"
x = txt.lower()
print(x) # hello my friends!

# converts a string into upper case.
txt = "Hello my friends!"
x = txt.upper()
print(x) # HELLO MY FRIENDS!

# converts the first character of each word to upper case.
txt = "Welcome to my world!"
x = txt.title()
print(x) # Welcome To My World!

# returns a string where a specified value is replaced with a specified value.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) # I like apples

# splits the string at the specified separator, and returns a list.
txt = "welcome to the jungle"
x = txt.split()
print(x) # ['welcome', 'to', 'the', 'jungle']

# swaps cases, lower case becomes upper case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) # hELLO mY nAME iS peter