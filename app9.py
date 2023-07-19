# Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default response.
def handle_exceptions(default_response):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Exception occurred: {e}")
                return default_response
        return wrapper
    return decorator

@handle_exceptions(default_response="An error occured!")


def divide_number(x, y):
    return x / y



result = divide_number(7, 0)
print("Result: ", result)