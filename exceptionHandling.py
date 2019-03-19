# Error and exception handling 
# accept a number and prints its square

def print_square():
    while True:
        try:
            number = int(input('Enter a number: '))
        except:
            print('You have entered a non-numeric value')
            continue
        else: 
            print(f'Square of {number} is {number**2}')
            break
        finally:
            print('Thank you\n')

print_square()

