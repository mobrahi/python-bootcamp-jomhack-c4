# text = "Python programming"

# print(text[0]) # first character
# print(text[-1]) # last character
# print(text[0:6]) # first 6 characters
# print(text[:8]) # first 8 characters
# print(text[8:]) # from index 8 to end

# name = " Bob the Builder "
# print(len(name)) # length of the string
# print(name.strip()) # remove leading/trailing whitespace
# print(len(name)) # length after stripping
# print(name.upper()) # convert to uppercase
# print(name.lower()) # convert to lowercase
# print(name.title()) # convert to title case
# print(name.replace("Bob", "Jane")) # replace substring

# name = "John Doe"
# age = 28

# greeting = f"Hello, my name is {name} and I am {age} years old."
# print(greeting)
# info = "Name: {}, Age: {}".format(name, age)
# print(info)
# info_percent = "Name: %s, Age: %d" % (name, age)
# print(info_percent)

text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike.
"""

# print(text.count("Python")) # count occurrences of "Python"
# print(text.count(",")) # count occurrences of ","

text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(' ', ''))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"Character count (including spaces): {char_count}")            # 239
print(f"Character count (excluding spaces): {char_count_no_spaces}")  # 204
print(f"Word count: {word_count}")                                    # 38
print(f"Sentence count: {sentence_count}")                            # 5