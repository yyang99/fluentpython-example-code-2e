from registration_param_2_module_registry import register


@register('key1')  # <8>
def f1():
    print('key1')


@register('key2')  # <9>
def f2():
    print('key2')


def f3():
    print('running f3()')
