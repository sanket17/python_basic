# for loop  

print('Normal While loop:')
mylist = [1,2,3,4,5,6,7,8,9]

for num in mylist:
    print(num)

print('Use of _ at variable name place:')
for _ in 'Hello':
    print('Hello World')

mytuple = (1,2,3)

for tup in mytuple:
    print(tup)

#tuple unpacking
print('Tuple Unpacking')

packTup = [(1,2), (3,4), (5,6), (7,8), (9,10)]
print(packTup)

print('Before Unpacking')
for record in packTup:
    print(record)

print('After Unpacking')
for (a,b) in packTup:
    print(a)
    print(b)

# the above loop can also be written in following way
# for a,b in packTup:
#     print(a)

# for loop using dictionaries
print('Looping dictionaries')
mydict = {'k1': 1, 'k2': 2, 'k3':3}

print('Printing only keys using normal syntax:')
for item in mydict:
    print(item)

print('Printing key-value in tuple format using dictVaribale.items() method:')
for item in mydict.items():
    print(item)

print('Printing key-value separetly use dictVaribale:')
for key,value in mydict:
    print(value)   

print('Printing key-value in seperately using dictVaribale.items() method:')
for key, value in mydict.items():
    print(f"{key} - {value}")

print('Printing only values using dictVaribale.values() method:')
for value in mydict.values():
    print(value)

print('Printing only keys using dictVaribale.keys() method:')
for key in mydict.keys():
    print(key)

# While loop
print('While loop in python')

x = 0

while x < 5:
    print(f"{x} is less than 5")
    x += 1
else:
    print("Loop gets finished")

# Useful operator 
# range
print('Range operator')

for num in range(0, 11, 2):
    print(num)

# enumerate

word = 'letter'
print('Before using enumerate')
index_count = 0
for letter in word:
    print(f"At {index_count} is {letter}")
    index_count += 1

print('\n After using enumerate')
for index, letter in enumerate(word):
    print(f"At {index} is {letter}")

# zip
print('\nzip operator')

list1 = [1,2,3,4,5]
list2 = ['a','b','c']

print('Printing tuple form of zip')
for items in zip(list1, list2):
    print(items)

print('\nPrinting tuple form of zip and changing order of list')
for l1,l2 in zip(list2, list1):
    print(f"{l1} -> {l2}")

# in operator
print('\nin operator using list')

from random import shuffle
shuffle(list1)
print(list1)

from random import randint

random_number = randint(0, 100)
print(f"Random number: {random_number}")


random_number = randint(0, 100)
print(f"Random number: {random_number}")

#List Comprehension
mylist = []
print('Creating list without list comprehension:')

for num in range(1,10):
    mylist.append(num*100)

print(mylist)

#creating same list using list comprehension

print('Creating list with list comprehension:')
mylist = []
mylist = [num for num in range(1, 10)]
print(mylist)

#creating list using list comprehension with condition
print('Creating list using list comprehension with condition:')
mylist = []
mylist = [num**2 for num in range(1, 10) if num%2 == 0]
print(mylist)

#nesting loop using list comprehension
print('Nested loop using list comprehension:')
mylist = []
mylist = [num*y for num in range(1, 10) for y in range(100,1100, 100)]
print(mylist)