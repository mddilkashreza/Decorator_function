def decorator(func):
    def wrap(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")


        result = func(*args, **kwargs)


        print(f"{func.__name__} returned: {result}")


        return result
    return wrap

@decorator
def multiply_numbers(x,y):
    return x * y

result = multiply_numbers(23,12)
print("Result: ", result)