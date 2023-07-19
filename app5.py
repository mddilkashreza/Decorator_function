def validate_arguments(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid argument passed to the function")
        return wrapper
    return decorator


@validate_arguments(lambda x:x > 0)
def calculate_cube(x):
    return x**3


print(calculate_cube(5))
print(calculate_cube(-3))