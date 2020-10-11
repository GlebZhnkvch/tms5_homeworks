from datetime import datetime

time = datetime.now()


def time_decorator(time_func):
    def some_function():
        print('Execution time of this func is:')
        result = time_func()
        print('Function completed successfully!')
        return result

    return some_function()


@time_decorator
def time_():
    print(time)
