from pyinject import Dependency, SingletonDependency


def test_no_args_dependency():
    class NoArgs:
        def __init__(self):
            pass

    obj = Dependency(NoArgs).inject()

    assert isinstance(obj, NoArgs)


def test_with_args_dependency():
    class WithArgs:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    arg1 = 1
    arg2 = "Hello"

    obj = Dependency(WithArgs, arg1, arg2).inject()
    assert isinstance(obj, WithArgs)
    assert obj.arg1 == arg1
    assert obj.arg2 == arg2


def test_no_args_dependency_singleton():
    class NoArgs:
        def __init__(self):
            pass

    dependency = SingletonDependency(NoArgs)
    obj1 = dependency.inject()
    obj2 = dependency.inject()

    assert isinstance(obj1, NoArgs)
    assert isinstance(obj2, NoArgs)
    assert obj1 == obj2


def test_with_args_dependency_singleton():
    class WithArgs:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    arg1 = 1
    arg2 = "Hello"

    dependency = SingletonDependency(WithArgs, arg1, arg2)
    obj1 = dependency.inject()
    obj2 = dependency.inject()

    assert isinstance(obj1, WithArgs)
    assert isinstance(obj2, WithArgs)
    assert obj1.arg1 == arg1
    assert obj1.arg2 == arg2
    assert obj2.arg1 == arg1
    assert obj2.arg2 == arg2
    assert obj1 == obj2


