# Example for function as object

def hello():
    print('Hello World')

hello()

print(hello)

greet = hello

print('After deleting hello() function')
del hello
print('Calling greet() after deleting hello')
greet()
#hello()

def original_func():
    print('This is original function')

def decorator_func(some_func):
    def wrapper_func():
        print('This is starting of wrapper function')
        some_func()
        print('This is end of wrapper function')

    return wrapper_func

new_decorated_func = decorator_func(original_func)
new_decorated_func()

# The above function can also be decorated as:
print('After adding @ operator')
@decorator_func
def original_func():
    print('This is original function')

original_func()

print('After removing @ operator')
#@decorator_func
def original_func():
    print('This is original function')

original_func()
