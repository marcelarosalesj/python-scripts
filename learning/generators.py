

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print('fib is type {}'.format(type(fib)))

fib_func = fibonacci
print('fib_func is type {}'.format(type(fib_func)))


print('Let\'s print first ten numbers in Fibonacci\'s sequence using fib:')
for i in range(10):
    print(next(fib))

print('Let\'s print more numbers:')
for i in range(10):
    print(fib.__next__())
