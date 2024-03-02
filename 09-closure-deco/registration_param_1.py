# tag::REGISTRATION_PARAM[]

registry = dict()  # <1>

def register(key):  # <2>
    def decorate(func):  # <3>
        print('running register'
              f'(key={key})->decorate({func})')
        registry[key] = func
        return func  # <6>
    return decorate  # <7>

@register('key1')  # <8>
def f1():
    print('key1')

@register('key2')  # <9>
def f2():
    print('key2')

def f3():
    print('running f3()')

# end::REGISTRATION_PARAM[]
if __name__ == "__main__":
    print(registry)