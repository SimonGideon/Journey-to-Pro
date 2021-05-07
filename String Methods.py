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

