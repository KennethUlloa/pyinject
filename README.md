# PyInject
Dependency injection library. Aims to be as simple as posible.

## Usage
Using `Dependency` will create the object in every call.
```python
# example.py
# import the dependency you need and the decorator 'inject'
from pyinject import Dependency, inject

class MyNeededDependency:
    def __init__(self, arg, other_arg):
        pass

# Supports *args and *kwargs
dependency = Dependency(MyNeededDependency,"some argument", other_arg="other arg")

@inject
def some_awesome_function(my_dependency: MyNeededDependency = dependency):
    # Do something cool with my_dependency
    pass
```
To use Singleton pattern 
```python
from pyinject import Dependency
class MyNeededDependency:
    pass
# Same code from above
# use is_singleton keyword argument
dependency = Dependency(MyNeededDependency, "one_argument", other_args=1, is_singleton=True)
# Same code
```
Take in count that `is_singleton` keyword argument is reserved and will be removed from the
kwargs dictionary passed to the dependency.

You might want to use another object to hold all of your dependency creators.
```python
# example.py
from pyinject import Dependency, DependantDependency, inject

class DB:
    pass


class Service:
    # No need to specify a default value, since it will be used 
    def __init__(self, db: DB):
        pass


class MyDependenciesHolder:
    # A simple dependency
    db = Dependency(DB, "connection_string", is_singleton=True)
    # Here a dependency can call another if the __init__ function is decorated with @inject
    service = DependantDependency(Service, db, is_singleton=True)

@inject
def some_func(service: Service = MyDependenciesHolder.service):
    pass
```
