# Notes stacked decorator vs decorator with parameters
#
#=================[ run at import time ]
#
#-----------------[ decorator with parameters ]
#
# @decorator_param(decorator_arg)
# def func(*args, **kwargs)
#   ...
#
# run at import time ===>
#      func = decorator_param(decorator_arg)(func)
#
#-----------------[ stacked decorators ]
#
# @decorator2
# @decorator1
# def func(*args, **kwargs)
#   ...
#
# run at import time ===>
#      func = decorator1(func)
#      func = decorator2(func)
#
#=================[ run at import time ]
#
# both at run time run ===> func(*args, **kwargs)
#
#

def first(f):
    print(f'apply first({f.__name__})')

    def inner1st(n):
        result = f(n)
        print(f'inner1({n}): called {f.__name__}({n}) -> {result}')
        return result
    return inner1st


def second(f):
    print(f'apply second({f.__name__})')

    def inner2nd(n):
        result = f(n)
        print(f'inner2({n}): called {f.__name__}({n}) -> {result}')
        return result
    return inner2nd

def register(key):  # <2>
    def decorate(func):  # <3>
        print(f'running register {func}(key={key})->decorate({func})')
        return func  # <6>
    return decorate  # <7>

def param_decorator(parameter):
    print(f'apply param_decorator({parameter})')
    def decorator(func):
        print(f'apply decorator({parameter})')
        def inner_decorator(n):
            result = func(n)
            print(f'inner_decorator({n}): called {func.__name__}({n}) -> {result}')
            return result

        return decorator
    return decorator

print("\n==================[ decorator with parameter ]")

@first
@second
def double(n):
    return n * 2

print("\n==================[ decorator with parameter ]")

@param_decorator("test parameter decorator")
def tripple(n):
    return n * 3

print("\n==================[ registration decorator with param ]")

@register("key1")
def quad(n):
    return n * 4