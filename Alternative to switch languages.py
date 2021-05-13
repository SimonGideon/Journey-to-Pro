def switch(value):
    if value == 1:
        return "one"
    if value == 2:
        return "Two"
    if value == 42:
        return " The answer to the question about life, the universe and everything"
    raise Exception("No case found!")
print(switch(1))
