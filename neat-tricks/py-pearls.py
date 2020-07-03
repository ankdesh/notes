# Awesome python shorthand tricks

* Apply a function to multiple objects and assign to new objects
```py
x_train, y_train, x_valid, y_valid = map(torch.tensor, (x_train, y_train, x_valid, y_valid))
```
