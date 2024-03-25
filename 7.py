import json
import functools


def jsoner(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        jsoned = json.dumps(result)
        return jsoned
    return wrapped


@jsoner
def lst():
    res = [1, 2, 3, 4]
    return res


@jsoner
def string():
    res = '1, 2, 3, 4'
    return res


@jsoner
def dictionary():
    res = {
        '123': 3,
        '456': 2,
        '789': 1
    }
    return res


print(lst())
print(string())
print(dictionary())
