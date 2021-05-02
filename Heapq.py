import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))
print(heapq.nsmallest(4, numbers))

people = [
    {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
    {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
    {'firstname': 'Joseph', 'lastname': 'Mwangi', 'age': 50},
    {'firstname': 'Lukas', 'lastname': 'Monk', 'age': 10},
    {'firstname': 'Victor', 'lastname': 'Waswa', 'age': 22},
    {'firstname': 'Wilson', 'lastname': 'Dedan', 'age': 12},

]
oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
mylist = [oldest, youngest]
for i in mylist:
    print(i)


# Smallest item in a collection.
heapq.heapify(numbers)
heapq.heappop(numbers)
print(numbers)
