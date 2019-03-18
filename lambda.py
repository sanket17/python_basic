# map function
# generate squqre of following list

num_list_1 = [1,2,3,4,5]

print(f'Given List: {num_list_1}')

def square_of_num(num):
    return num**2

square_list = list(map(square_of_num, num_list_1))
print(f'Square list: {square_list}')

#filter function 
# fetch even number from list

num_list_2 = [1,3,4,5,6,7]

print(f'Given list: {num_list_2}')

def even_number(num):
    return num%2

even_num_list = list(filter(even_number, num_list_2))
print(f'Even number list using filter: {even_num_list}')


# lamba expression convert above two problem statements using lambda expression

lambda_square_list = list(map(lambda num:num**2, num_list_1))
print(f'lambda expression using map() to convert given list into {lambda_square_list}')

lambda_even_list = list(filter(lambda num: num%2 == 0,num_list_2))
print(f'lambda expression using filter() to convert given list into {lambda_even_list}')

