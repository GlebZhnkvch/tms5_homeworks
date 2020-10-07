double_key_func = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})
print(double_key_func(abc=1, de=2))
