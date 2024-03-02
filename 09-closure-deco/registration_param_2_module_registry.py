# tag::REGISTRATION_PARAM[]

registry = dict()  # <1>

def register(key):  # <2>
    def decorate(func):  # <3>
        print('running register'
              f'(key={key})->decorate({func})')
        registry[key] = func
        return func  # <6>
    return decorate  # <7>

