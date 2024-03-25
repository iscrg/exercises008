import functools
from datetime import datetime


def excepter(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            with open('log.txt', 'a') as file:
                error = f'[{datetime.now()}] {type(e).__name__}: {e} \n'
                file.write(error)
    return wrapped


@excepter
def error():
    return 2 / 0


error()
