from pyinject import Dependency, DependantDependency, SingletonDependency
import datetime


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
            self.timestamp = datetime.datetime.now()

    dependency = Dependency(NoArgs, is_singleton=True)
    obj1 = dependency.inject()
    obj2 = dependency.inject()

    assert isinstance(obj1, NoArgs)
    assert isinstance(obj2, NoArgs)
    assert obj1.timestamp == obj2.timestamp


def test_with_args_dependency_singleton():
    class WithArgs:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    arg1 = 1
    arg2 = "Hello"

    dependency = Dependency(WithArgs, arg1, arg2, is_singleton=True)
    obj1 = dependency.inject()
    obj2 = dependency.inject()

    assert isinstance(obj1, WithArgs)
    assert isinstance(obj2, WithArgs)
    assert obj1.arg1 == arg1
    assert obj1.arg2 == arg2
    assert obj2.arg1 == arg1
    assert obj2.arg2 == arg2
    assert obj1 == obj2


def test_dependant_dependency():
    class A:
        def __init__(self):
            pass

    class B:
        def __init__(self, a: A):
            self.a = a
            pass

    a = Dependency(A)
    b = DependantDependency(B, Dependency(A))
    casdf = SingletonDependency(A).inject()
    type(casdf)
    obj1 = a.inject()
    obj2 = b.inject()

    assert isinstance(obj1, A)
    assert isinstance(obj2, B)
    assert isinstance(obj2.a, A)


def test_dependant_dependency_singleton():
    class A:
        def __init__(self):
            self.timestamp = datetime.datetime.now()

    class B:
        def __init__(self, a: A):
            self.a = a
            self.timestamp = datetime.datetime.now()

    a = Dependency(A)
    b = DependantDependency(B, a=Dependency(A), is_singleton=True)
    obj_a = a.inject()
    obj_b = b.inject()
    obj_b_1 = b.inject()

    assert isinstance(obj_a, A)
    assert isinstance(obj_b, B)
    assert isinstance(obj_b.a, A)
    assert obj_b.timestamp == obj_b_1.timestamp
    assert obj_b.a == obj_b_1.a




