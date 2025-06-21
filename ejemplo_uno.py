import time


def execution_time_decorator(func):
    """
    This is the decorator for logging the execution time for each
    functions of the calculator.

    input: function
    output: logged execution time of the function (string)
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tiempo de ejecución: {execution_time} segundos")
        return result
    return wrapper


@execution_time_decorator
def sum(num_1: int, num_2: int) -> int:
    # Returning the sum of both parameters
    return num_1+num_2


@execution_time_decorator
def substraction(x: int, y: int) -> int:
    # Returning the rest of both parameters
    return x-y


@execution_time_decorator
def mult(x: int, y: int) -> int:
    # Returning the multiplication of both parameters
    return x*y


@execution_time_decorator
def div(x: int, y: int) -> int:
    # Returning the division of both parameters
    return x/y


help(execution_time_decorator)

result = sum(5, 7)
print(f"Resultado de la suma: {result}")

