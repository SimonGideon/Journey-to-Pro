names = ['Alex', 'Emmanuel', 'Jayson', 'Maxwel']
print(names[0])  # The name in the first place.
print(names[3])  # The name int he second place.
print(names[-1])  # The first name from right hand.
names[0] = 'Luke' # Replaces the name 'Luke' an character 0.
print(names)
names.append('Samson') # Adds another name 'Samson'.
print(names)

names.insert(1, 'Angelah') # Inserts the name 'Angela' at position 1.
print(names)
names.remove('Jayson')
print(names)
print(names.index("Luke")) # Display the[position at which the name 'Luke' is located at the list.
print(len(names)) # Counts the length tof the list.
names.insert(3, ' Luke,' * 3)
print(names)
s = names.count('Luke') # counts how many times has 'Luke apeared', * by passes "' Luke, Luke, Luke,'"
print(s)
names.reverse() # reverses the order of the list.
print(names)

print(names.pop(-1))

# Dictionaries
state_capitals = {
    'Arkansas': 'Little Rock',
    'Clolorado': 'Denver',
    'Califonia': 'Sacramento',
    'Georgia': 'Atlanta'

}
ca_capital = state_capitals['Califonia']
print(ca_capital)
print("\n")
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))

# sets
first_names = {'Adams', 'Beth', 'Charles'}
names = set(first_names)
print(names)
if names in first_names: # checking members of the set using in:
    print(names)
print(len(names))



# Defaultdict
from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston')
print(state_capitals['Alabama'])
print(state_capitals['Arkansas'])
