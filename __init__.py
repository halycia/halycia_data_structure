"""
This package aims to gather all knowledge I gained in python this semester (2024.1)
while I was in a Data Structure course. Of course I also practiced these algorithms
with real world context, but this package only has the necessary tools to do so.
"""

# to alocate subpackages in this package, please see section 6.4 of python docs

# to each of the data structures available, there's a module(script) for it
# for every file name in conflict with other items not from this directory, please put item_halycia
# please put a documentation under each class and function of your modules

# section 6.4.1 of python Tutorial docs(https://docs.python.org/3/tutorial/index.html) says:

# The import statement uses the following convention: if a package’s __init__.py code 
# defines a list named __all__, it is taken to be the list of module names that should
# be imported when from package import * is encountered. It is up to the package author 
# to keep this list up-to-date when a new version of the package is released.

# please keep in mind that import all subitems from a package is a bad practice
# but you have it defined in __all__ just in case
# __all__ = ["echo", "surround", "reverse"] -> module names

__all__ = ["queue_halycia", "stack", "deque_halycia"]

# please keep in mind to not define a locally defined name the same as an imported module name
# otherwise the name will keep the module from beeing imported

# for the priority queue implementation, please see section 6.4.2

#I am aware I am not handling errors yet.