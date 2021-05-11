
# Catching multiple exceptions.
try:
    d = {}
    a = d[1]
    b = d.non_existing_field
except (KeyError, AttributeError) as e:
    print("A keyError or an AttributeError exception has been caught.")

# Else
try:
    data = {1: 'one', 2: 'two'}
    print(data[1])
except KeyError as e:
    print('Key not found')
else:
    raise ValueError()

# Example of exception handling.
while True:
    try:
        nb = int(input('Enter a number: '))
        break
    except ValueError:
        print('This is not a number, try again.')
d= [{7: 3}, {25: 9}, {38: 5}]

for i in range(len(d)):
    do_stuff(i)
    try:
        dic = d[i]
        i += dic[i]
    except KeyError:
        i += 1

resource = allocate_some_expensive_resources()
try:
    do_stuff(resource)
except SomeException as e:
    log_error(e)
    raise
finally:
    free_expensive_resource(resource)
try:
    5/0
except ZeroDivisionError:
    print("Got an error")
    raise

# Custom Exception
class CustomError(Exception):
    pass
x = 1
if x == 1:
    raise CustomError('This is custom error')


# Catch custom Exception.
class CustomError(Exception):
    pass
try:
    raise CustomError('Can you catch me?')
except CustomError as e:
    print('Catched CustomError :{}'.format(e))
except Exception as e:
    print('Generic exception: {}'.format(e))
    
