from typing import Type, TypeVar, Generic

T = TypeVar("T")


class Dependency(Generic[T]):
    """
    Class representing dependencies, it holds a type and the related data to
    instantiate that type. The instantiation takes part in *inject* method
    Parameters:
        some_type: Type[T] the class that is going to be injected
        args: positional arguments for the class
        kwargs: keyword arguments for the class
    Note:
        'is_singleton' is a reserved key for the class, it will be removed from the
        kwargs dictionary. Is used to set the flag 'singleton' to determine whether to
        save the inject result or not.
    """

    def __init__(self, some_type: Type[T], *args, **kwargs):
        self.some_type = some_type
        self.args = args
        self.kwargs = kwargs
        if "is_singleton" in kwargs:
            self.singleton = kwargs.pop("is_singleton")
        else:
            self.singleton = False
        self.instance: T = None

    def inject(self) -> T:
        """
        Creates the specified type with stored arguments
        Returns:
            instance of T
        """
        if self.singleton:
            if not self.instance:
                self.instance = self.some_type(*self.args, **self.kwargs)
            return self.instance
        else:
            return self.some_type(*self.args, **self.kwargs)


class DependantDependency(Dependency[T]):
    """
    Searches through the provided arguments to find whether it contains dependency objects.
    If so, then it will call the inject method on each of them and replaced them with the injected dependency
    """

    def __init__(self, some_type: Type[T], *args, **kwargs):
        super().__init__(some_type, *args, **kwargs)

    def process_arg(self, arg):
        if isinstance(arg, Dependency):
            return arg.inject()
        return arg

    def inject(self) -> T:
        new_args = tuple([self.process_arg(arg) for arg in self.args])
        new_kwargs = self.kwargs.copy()
        for k in new_kwargs:
            new_kwargs[k] = self.process_arg(new_kwargs[k])
        if not self.singleton:
            return self.some_type(*new_args, **new_kwargs)
        else:
            if not self.instance:
                self.instance = self.some_type(*new_args, **new_kwargs)

            return self.instance
