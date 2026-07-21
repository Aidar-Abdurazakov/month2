import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter() 

        result = func(*args, **kwargs)  

        end = time.perf_counter()  

        print(f"Функция {func.__name__} работала {end - start:.2f} секунды")

        return result

    return wrapper


@timer
def calculate_sum(n):
    return sum(range(n))


result = calculate_sum(1_000_000)
print(result)