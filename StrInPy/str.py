

 
# String methods and their usage
sample_string = "Hello World!"

# capitalize(): Converts the first character to uppercase
print("capitalize():", sample_string.capitalize())  # Output: Hello, world!

# casefold(): Converts string into lower case
print("casefold():", sample_string.casefold())  # Output: hello, world!

# center(width[, fillchar]): Returns a centered string
print("center():", sample_string.center(20, "*"))  # Output: ****Hello, World!****

# count(sub[, start[, end]]): Returns the number of occurrences of a substring
print("count():", sample_string.count("l"))  # Output: 3

# encode(encoding="utf-8", errors="strict"): Returns an encoded version of the string
print("encode():", sample_string.encode())  # Output: b'Hello, World!'

# endswith(suffix[, start[, end]]): Checks if a string ends with a specified suffix
print("endswith():", sample_string.endswith("!"))  # Output: True

# expandtabs(tabsize=8): Sets the tab size of the string
print("expandtabs():", "Hello\tWorld".expandtabs(2))  # Output: Hello World

# find(sub[, start[, end]]): Searches the string for a specified substring
print("find():", sample_string.find("World"))  # Output: 7

# format(*args, **kwargs): Formats string into a nicer output
print("format():", "My name is {} and I am {}".format("Alice", 30))  # Output: My name is Alice and I am 30

# format_map(mapping): Similar to format(), but accepts a mapping object
print("format_map():", "My name is {name} and I am {age}".format_map({"name": "Bob", "age": 25}))  # Output: My name is Bob and I am 25

# index(sub[, start[, end]]): Like find(), but raises ValueError when substring is not found
print("index():", sample_string.index("World"))  # Output: 7

# isalnum(): Checks if all characters in the string are alphanumeric
print("isalnum():", sample_string.isalnum())  # Output: False

# isalpha(): Checks if all characters in the string are alphabetic
print("isalpha():", sample_string.isalpha())  # Output: False

# isascii(): Checks if the string contains only ASCII characters
print("isascii():", sample_string.isascii())  # Output: True

# isdecimal(): Checks if all characters in the string are decimals
print("isdecimal():", sample_string.isdecimal())  # Output: False

# isdigit(): Checks if all characters in the string are digits
print("isdigit():", sample_string.isdigit())  # Output: False

# isidentifier(): Checks if the string is a valid identifier
print("isidentifier():", sample_string.isidentifier())  # Output: False

# islower(): Checks if all characters in the string are lowercase
print("islower():", sample_string.islower())  # Output: False

# isnumeric(): Checks if all characters in the string are numeric
print("isnumeric():", sample_string.isnumeric())  # Output: False

# isprintable(): Checks if all characters in the string are printable
print("isprintable():", sample_string.isprintable())  # Output: True

# isspace(): Checks if all characters in the string are whitespaces
print("isspace():", sample_string.isspace())  # Output: False

# istitle(): Checks if the string follows the rules of a title
print("istitle():", sample_string.istitle())  # Output: False

# isupper(): Checks if all characters in the string are uppercase
print("isupper():", sample_string.isupper())  # Output: False

# join(iterable): Joins the elements of an iterable to create a string
print("join():", "-".join(["Hello", "World"]))  # Output: Hello-World

# ljust(width[, fillchar]): Returns a left-justified string
print("ljust():", sample_string.ljust(20, "*"))  # Output: Hello, World!*******

# lower(): Converts all characters in the string to lowercase
print("lower():", sample_string.lower())  # Output: hello, world!

# lstrip([chars]): Removes leading whitespace or specified characters
print("lstrip():", "    Hello, World!".lstrip())  # Output: Hello, World!

# maketrans(x[, y[, z]]): Returns a translation table
translation_table = sample_string.maketrans("el", "XY")
print("maketrans():", sample_string.translate(translation_table))  # Output: HXYlo, World!

# partition(sep): Returns a tuple containing the original string, the separator, and the part after the separator
print("partition():", sample_string.partition(","))  # Output: ('Hello', ',', ' World!')

# replace(old, new[, count]): Replaces a specified substring with another substring
print("replace():", sample_string.replace("World", "Universe"))  # Output: Hello, Universe!

# rfind(sub[, start[, end]]): Searches the string for a specified substring from the end
print("rfind():", sample_string.rfind("o"))  # Output: 8

# rindex(sub[, start[, end]]): Like rfind(), but raises ValueError when substring is not found
print("rindex():", sample_string.rindex("o"))  # Output: 8

# rjust(width[, fillchar]): Returns a right-justified string
print("rjust():", sample_string.rjust(20, "*"))  # Output: *******Hello, World!

# rpartition(sep): Returns a tuple containing the part before the separator, the separator, and the rest of the string
print("rpartition():", sample_string.rpartition(","))  # Output: ('Hello', ',', ' World!')

# rsplit(sep=None, maxsplit=-1): Splits the string from the right
print("rsplit():", sample_string.rsplit(","))  # Output: ['Hello', ' World!']

# rstrip([chars]): Removes trailing whitespace or specified characters
print("rstrip():", "Hello, World!    ".rstrip())  # Output: Hello, World!

# split(sep=None, maxsplit=-1): Splits the string into a list
print("split():", sample_string.split(","))  # Output: ['Hello', ' World!']

# splitlines([keepends]): Splits the string at line breaks
multi_line_string = "Hello\nWorld\n"
print("splitlines():", multi_line_string.splitlines())  # Output: ['Hello', 'World']
