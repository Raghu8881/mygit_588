'''x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)'''
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
x = fib(5)
print(x.__next__())
