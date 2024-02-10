from functools import wraps
from inspect import signature
from .dependency import *


def inject(f):
    """
    Decorator that search all Dependency defaults in the decorated function parameters.
    Behind the scenes, it will call the inject method to create the desired object in the
    corresponding parameter.
    """
    @wraps(f)
    def decorated_func(*args, **kwargs):
        params = signature(f).parameters

        for name in kwargs:
            value = kwargs[name]
            if isinstance(value, Dependency):
                dep = value.inject()
                kwargs[name] = dep

        for param in params.values():
            default = param.default
            if isinstance(default, Dependency):
                dep = default.inject()
                kwargs[param.name] = dep

        result = f(*args, **kwargs)

        return result

    return decorated_func
