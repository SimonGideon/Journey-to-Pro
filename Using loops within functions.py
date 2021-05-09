# Return the statement inside loop in a function.
def func(params):
    for value in params:
        print('Got value {}'.format(value))

        if value == 1:
            # returns from the function as soon as value is 1.
            print(">>>>>>> Got 1")
            return
        print("still looping")
    return \
        print("Couldn't find 1")


func([5, 3, 2, 8, 9])
