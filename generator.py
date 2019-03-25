# Manual function to generate cube of series

def cubic(n):
    result = []
    for num in range(0,n):
        result.append(num**3)
    return result

op_list = cubic(10)
print(op_list)

# convert above function in generator

def cubic_generator(n):
    for x in range(n):
        yield x**3

for num in cubic_generator(10):
    print(num)

# To convert generator in list
generator_list = list(cubic_generator(10))
print(generator_list)

# using next() to get next value of generator
generator_variable = cubic_generator(10)
print('Printing generator variable{}'.format(generator_variable))
print(next(generator_variable))

# use next() function on str
str_var = 'Hello'
print(str_var)

str_var_iter = iter(str_var)
print(next(str_var_iter))