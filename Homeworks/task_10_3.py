def decorator_for_check_func(func):
    def wrapper(nums):
        try:
            new_nums = [element for element in nums if element % 2]
            return func(new_nums)
        except TypeError:
            print('Please enter a list with nums!')
    return wrapper


@decorator_for_check_func
def check_func(list_for_nums_check) -> list:
    print(list_for_nums_check)


check_func([1, 4, 8, 10, 11])




