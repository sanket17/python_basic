# ordered dict

mydict = {}
mydict['a'] = 1
mydict['b'] = 2
mydict['c'] = 3

for k,v in mydict.items():
    print(k, v)

from collections import OrderedDict

mydict = OrderedDict()
mydict['a'] = 1
mydict['b'] = 2
mydict['c'] = 3

print('After using ordered dict:\n')

for k,v in mydict.items():
    print(k, v)

# namedtuple

mytup = (1,2,3)
print('Fetching tuples using indexes: {}'.format(mytup[0]))

print('Creating tuple using namedtuple:\n')

from collections import namedtuple

tup_var = namedtuple('TupVar','name age')
mytup = tup_var(name='Sanket', age=26)

print('Printing tuple value using namedtuple: {}'.format(mytup.name))

# pyhton debugger
import pdb

x = [1,3,4,5]
y = 2
z = 3

pdb.set_trace()

#timeit module

# Suppose we want to generate a string as 1-2-3-..-99

s1 = "-".join(str(n) for n in range(100))
print(s1)
print('Print time for its execution: ')
import timeit

s1_time = timeit.timeit('"-".join(str(n) for n in range(100))', number=1)
print('Time required to generate string s1 is: {}'.format(s1_time))
s2_time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1)
print('Time required to generate string s2(list) is: {}'.format(s2_time))
s3_time = timeit.timeit('"-".join(map(str,range(100)))', number=1)
print('Time required to generate string s3(map) is: {}'.format(s3_time))

# Regular expression

pattern = ['Hello', 'hola']
str1 = 'Hello World'
str2 = 'Hola Mundo'

import re

result1 = re.match(pattern[1], str1)
print('Type of unmatched object: ')
type(result1)
print('Result of 1st match: {}'.format(result1))

result2 = re.match(pattern[0], str1)
print('Type of unmatched object: ')
type(result2)
print('Result of 2nd match: {}'.format(result2))
print('Starting index of the match: {}'.format(result2.start()))
print('End index of the match: {}'.format(result2.end()))

print

slpit_result = str1.split()
print('Result of slipt(0 method: {}'.format(slpit_result))

# StringIO 
message = 'Londen has fallen, as well as olympus has fallen'

from io import StringIO 


with StringIO.StringIO(message) as new_file:
    print(new_file.readlines())



