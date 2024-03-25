def print_result(func):
    def wrapped(arg):
        result = func(arg)
        print(result)
        return result
    return wrapped


@print_result
def square(x):
    return x ** 2


square(5)
