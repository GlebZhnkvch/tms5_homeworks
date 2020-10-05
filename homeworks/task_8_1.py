def function_one_arg(arg_list_):
    try:
        arg_list_ = set(arg_list_)  # Convert to set
        return arg_list_
    except TypeError:
        return (f'Please, enter the list, you entered: {arg_list_}')


print(function_one_arg([1, 2, 3, 5, 1]))
