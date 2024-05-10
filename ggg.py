def null_decorator(func, uu:str) -> str:
    return func

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def greet():
    return 'Hello!'


@uppercase
def greet():
    return 'Hello!'

print(greet())