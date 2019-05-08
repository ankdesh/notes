## Types of methods in a class
* __Class Method:__ The @classmethod decorator is a builtin function decorator that is an expression that is bound to the class and not
the object of the class and ___can___ modify the state of the class.
* __Class Method:__ The __@staticsmethod__ decorator is a builtin function decorator that is an expression that is bound to the class and not
the object of the class and ___cannot___ modify the state of the class. Static method function can be defined outside the class 
and will work perfectly, it is generally added to the class for modularity.
* __Instance Method:__ Can access instance of the class and also change state of class using self.__class__ method 


```py
class MyClass:
    
    classVar = 15
    
    def __init__ (self):
        self.objVar = 10
    
    
    def method(self):
        self.objVar = 20
        self.__class__.classVar = 100
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
        
Result:
1000
100
'static method called'
```

## Getters and Setters in Python
* @property and 
```py
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
c = Celsius()
c.temperature = 100
print (c.temperature)
c.temperature = -300

Result:
Setting value
Getting value
100
ValueError: Temperature below -273 is not possible

```
