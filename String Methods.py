# Changing the capitalization of strings.
n="This iS Our Wedding DAy"
print("this Is A 'String'.".capitalize())
print(str.swapcase(n))
print(str.upper(n))

# Translating Character into string.
translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
print(translated)

# String module's useful constants.
import string

print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)
print(string.printable)
print(n.title())

# Stripping unwanted leading characters from a string.
print("    spacious string    ".rstrip())

# Reversing a string.
print(reversed('hello'))
print([char for char in reversed('hello')])
print(''.join(reversed('hello my people')))

def reversed_sting(main_string):
    return main_string[::-1]
print(reversed_sting('hello'))

# Splitting a string based on a delimiter into a list of strings.
print("This is a sentence.".split())
print("This is a sentence.".split('e', maxsplit=0))
print("This is a sentence.".split('e', maxsplit=1))
print("This is a sentence.".split('e', maxsplit=2))
print("This is a sentence.".split('e', maxsplit=-1))
print("This is a sentence.".rsplit('e', maxsplit=1))

# Replacing all occurrences of one substring with another substring.
"""To replace 'foo' with 'spam'"""
print("Make sue to spam your sentences.".replace('foo', 'spam'))

# Testing what a string is composed of.
print("Hello World".isalpha())
print("HeLLO WORLD".isupper())
print("HELLO WORLD".isupper())
print("HeLLO WORLD".islower())
n = str.lower("HELLO WORLD")
print(n.islower())
m = str.title(n)
print(m.istitle())
print("3A".isalnum())
print("\t\r\n".isspace())
my_str = ''
print(my_str.isspace())
print(my_str.isspace() or not my_str)

# String Contains.
print("foo" in "foo.baz.bar")

# Joining a list of strings into string.
print(" ".join(["once","upon", "a", "time"]))
print("_____".join(["once", "upon", "a", "time"]))

# Counting number of times a substring appears in string.
s = "She sells seashells by the sea shores"
print(s.count('sh'))
print(s.count("se"))

# Case insensitive string comparison.
import unicodedata
print([unicodedata.name(char) for char in "e^"])

import unicodedata
def normaliza_case(text):
    return unicodedata.normalize("NFKD", text.casefold())
def caseless_equal(left, right):
    return normalize_case(left) == normalize_case(right)


# Justify Strings
interstances_lenghts = {
    5: (1381, 2222),
    19: (63, 102),
    40: (2555, 4112),
    93: (189, 305),

}
for road,length in interstances_lenghts.items():
    miles,kms = length
    print('{} -> {} mi. ({} km.)'.format(str(road).rjust(4), str(miles).ljust(4), str(kms).ljust(4)))


# Testing the starting and ending character of a string.
s = "This is a test string."
print(s.startswith("T"))
print(s.endswith('.'))
print(s.endswith('stop.'))

# Conversion between str or bytes data and unicode characters.
