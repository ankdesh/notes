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
