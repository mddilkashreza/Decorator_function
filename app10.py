# Write a Python program that implements a decorator to enforce type checking on the arguments of a function
import inspect


def enforce_type_checking(func):
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        parameters = signature.parameters


        for i, arg in enumerate(args):
            param_name = list(parameters.keys())[i]
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be type '{param_type.__name__}'")
            

        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type '{param_type.__name__}'")
            
        
        return func(*args, **kwargs)
    return wrapper



@enforce_type_checking
def multiply_number(x: int, y:int) -> int:
    return x * y


result = multiply_number(5, 7)
print("Result: ", result)


result = multiply_number("5", 7)