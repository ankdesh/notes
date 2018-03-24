# Python list and map comprehensions

* Creates a list of (index, x[0], x[1]) where x is each element of stateTable
```py
list(enumerate((x[0],x[1]) for x in stateTable))
```

* Create a map from x[0] to (x[1],x[2]) 
```py
{x[0]:(x[1],x[2]) for x in stateTable}
```

* Indices for which (x[-1]-x[-2]+1  for x in stateTable) condition passes value > 1
```py
[index for index,value in enumerate(x[-1]-x[-2]+1  for x in stateTable) if value > 1 ]
``` 

* Nested list comprehension
```py
[[float(y) for y in x] for x in l]
Equivalent for 
newList = []
for x in l:
  for y in x:
    newList.append(float(y))
```

* Zip fucntion. zip function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
```py
 x = [1, 2, 3]
 y = [4, 5, 6]
 zipped = zip(x, y) # Zips x and y lists to create a list (x,y) tuples
 x2, y2 = zip(*zipped) # Unzips to x2, y2 lists
```
 
* Use zip to create map enumeration
```py
{number: letter for letter, number in zip('ankur',range(1,10))}
{1: 'a', 2: 'n', 3: 'k', 4: 'u', 5: 'r'}
``` 
 
* List enum in map enum   
```py
    {
     'asd1':[n for n in range(1,100) if n%9 == 0],
     'asd2':[n for n in range(1,100) if n%7 == 0]
    }
  
    {'asd1': [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
     'asd2': [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]}
```py
