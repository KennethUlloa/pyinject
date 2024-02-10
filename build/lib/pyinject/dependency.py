from typing import Type, TypeVar, Generic

T = TypeVar("T")


class Dependency(Generic[T]):
    """
    Class representing dependencies, it holds a type and the related data to
    instantiate that type. The instantiation takes part in *inject* method
    """

    def __init__(self, some_type: Type[T], *args, **kwargs):
        self.some_type = some_type
        self.args = args
        self.kwargs = kwargs

    def inject(self) -> T:
        """
        Creates the specified type with stored arguments
        Returns:
            instance of T
        """
        return self.some_type(*self.args, **self.kwargs)


class SingletonDependency(Dependency[T]):
    """
    Singleton approach for dependency. It creates the instance and saves it so
    the next time it's called, it will return the saved object
    """

    def __init__(self, some_type: Type[T], *args, **kwargs):
        super().__init__(some_type, *args, **kwargs)
        self.instance = None

    def inject(self) -> T:
        if not self.instance:

            self.instance = super().inject()
        return self.instance


