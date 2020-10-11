def decorator_for_reverse_args_func(func):
    def wrapper(*args):
            new_args = [element for element in args[::-1]]
            return func(new_args)
    return wrapper


@decorator_for_reverse_args_func
def reverse_args_func(args):
    print(args)


reverse_args_func([1], 'a', 3, 8, (1, 2, 3))

