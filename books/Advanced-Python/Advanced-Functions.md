## Callable Function objects (to implement function with states)
* Implementing a __call__() functions in a class makes its objects callable e.g.

```py
class Record:
    def __init__(self, str):
        self._str = str
        self._show = True
    
    def __call__(self):
        if self._show:
            print (self._str)
        else:
            print ('No Show')
    
    def invert_show(self):
        self._show = False if self._show==True else True
        
rec = Record('Ankur')
rec()
rec.invert_show()
rec()
rec.invert_show()
rec()

Result:
Ankur
No Show
Ankur
``` 
* Classes are callables. Calling a class invokes the constructor 
```py
callable (Record)

Result:
True
```

## Clousure
* A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. For example, in case of a nested function, where outer function returns the inner function, inner function will maintain the values captured from the body of outer function, even after the outer function has returned.
```py
def outer_function():
    x = 10 # This should go out of scope when outer_function returns
    def inner_function():
        print (x) # Then how will this execute when inner_function is called outside
    return inner_function

inn_func = outer_function()
inn_func() # Magic or closure ?

Result:
10
```

## Decorators 
A decorator is a function which takes a functions and returns one. This allows to do simple modifications to Callables without intrusion. In the following example, we report an error if the input argument to function is negative
```py
def check_neg(old_function):
    def new_function(arg):
        if arg < 0: 
            raise ValueError("Negative Argument")
        return old_function(arg)
    return new_function
 
@check_neg
def square(x):
    return x*x

print(square(2))
print(square(-2))

Result:
4
ValueError: Negative Argument
```

When we need decorator to take input a value too
```py
def multiply(multiplier):
    def multiply_generator(old_func):
        def new_func(*args, **kwds):
            return multiplier * old_func(*args, **kwds)
        return new_func
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

return_num(5)

Result:
15
```
