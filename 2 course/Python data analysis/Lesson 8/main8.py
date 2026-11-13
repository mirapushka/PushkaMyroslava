import functools

def validate_positive_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)):
                if arg <= 0:
                    raise ValueError("Аргументи повинні бути додатними числами")
        return func(*args, **kwargs)
    return wrapper

@validate_positive_numbers
def get_area(a, b):
    
    return a * b

if __name__ == "__main__":

    print("Площа:", get_area(5, 10)) 

    try:
        print(get_area(-3, 4))
    except ValueError as e:
        print("Помилка:", e)