## Making Python module searchable

1. Add to sys.path using sys.path.append('dir_name')
1. Add to PYTHONPATH variable in the bash environment. It adds the paths to sys.path when the pythn starts

## Creating a package in Python

__Module__ A module is a single file (or files) that are imported under one import and used. 

__Package__ A package is a collection of modules in directories that give a package hierarchy.

```py
import my_module # Module
from my_package.abc.bcd import my_module
```

* The top level directory defines the package and should be there in sys.path
* Directories with __init__.py file inside create a module. The __init__.py are executed with the modules are imported. 
* To check the onit file, run <module_name>.__file__ in python. 
* To import a class ABC in the abc.py file in the xyz module, you need to use 
```py 
import xyz
var1 = xyz.abc.ABC()
```
To make the above case simpler, add ```from xyz.abc import ABC``` to abc/__init__.py file. Then the class can be accessed as 
```py 
import xyz
var1 = xyz.ABC()
```
## Executing direcrtories
A package can be made directly executable in python by adding __main__.py file to top level package folder.

