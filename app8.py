# Write a Python program that implements a decorator to add logging functionality to a function.


def add_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs:{kwargs}")


        result = func(*args, **kwargs)


        print(f"{func.__name__} returned: {result}")


        return result
    return wrapper

@add_logging

def add_number(x, y):
    return x + y


result = add_number(444, 555)
print("Result: ", result)