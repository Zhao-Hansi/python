import functools


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('装饰器1')
        return func(*args, **kwargs)
    return wrapper


@repeat(4)
@log_execution_time
def greet(message):
    print(message)


if __name__ == '__main__':
    greet('hello world')
