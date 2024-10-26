from functools import lru_cache
@ru_cache(maxsize=100) # caches up to 100 unique calls
def fibonacci (n) :
  if n< 2：
      return n
  return fibonacci(n - 1) + fibonacci(n - 2)


from functools import partial
def multiply(a, b):
  return a * b
double = partial(multiply, 2)
# 'double' now multiplies any input by 2

print(double(5)) # Output: 10

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y,
numbers) # Multiplies all elements in the list
print( result) # Output: 24

from functools import wraps
def my_decorator (func) :
    @wraps (func)
      def wrapper(*args, **kwargs):
         print( "Something is happening before the function is called." )
         result = func(*args, **kwargs)
         print( "Something is happening after the function is called.")
        return result
     return wrapper

@my_decorator
def say_hello():
    print( "Hello!")

say_hello() # Keeps the original function's metadata


