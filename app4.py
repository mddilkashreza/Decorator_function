def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())


        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        

        result = func(*args, **kwargs)

        cache[key] = result

        return result
    
    return wrapper



@cache_result
def calculate_multiple(x, y):
    print("Calculating the product of two numbers...")
    return x * y

print(calculate_multiple(4,4))
print(calculate_multiple(4,4))
print(calculate_multiple(5,5))
print(calculate_multiple(3,5))
print(calculate_multiple(4,9))
print(calculate_multiple(4,9))
print(calculate_multiple(-5,5))
print(calculate_multiple(-6,5))