####################################################################
#
#  Stacked Decorator vs Decorator With Parameters
#
# =================[ run at import time ]===========================
#
# -----------------[ decorator with parameters ]--------------------
#
# @decorator_param(decorator_arg)
# def func(*args, **kwargs)
#   ...
#
# run at import time ===>
#      func = decorator_param(decorator_arg)(func)
#
# -----------------[ stacked decorators ]---------------------------
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
# =================[ run at import time ]===========================
#
# both at run time run ===> func(*args, **kwargs)
#
###################################################################

print("\n######################################### [ at Import Time ]")


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


def register_decorator(key):
    def decorate(func):
        print(f'running register {func}(key={key})->decorate({func})')  # <1> <=== this will run at import time
        return func  # <2> <=== this will return original func without replace it

    return decorate


def param_decorator(parameter):
    print(f'apply param_decorator({parameter})')

    def decorator(func):
        print(f'apply decorator({parameter})')
        decorator_var = 99

        def inner_decorator(n):  # <2> <=== this inner_decorator is a new function which will replace func(),
            result = func(n)
            print(
                f'inner_decorator({n}): called {func.__name__}({n}) -> {result}')  # <1> <=== this will not run at import time
            print(
                f"function closure inner_decorator has free variable decorator_var = {decorator_var}")  # <3> function inner_decorator can be a closure have free variables from outer function
            return result

        return inner_decorator

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


@register_decorator("key1")
def quad(n):
    return n * 4


if __name__ == '__main__':
    n = 9
    print("\n######################################### [ at Run Time ]")

    print(f"double({n}) = {double(n)}")
    print("\n--------------------------")

    print(f"tripple({n}) = {tripple(n)}")
    print("\n--------------------------")

    print(f"quad({n}) = {quad(n)}")
    print("\n--------------------------")
