import functools


def log_execution(func):
  """Декоратор, який логує виклик функції, її аргументи та результат."""

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print(f"Виклик функції '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
    result = func(*args, **kwargs)
    return result

  return wrapper


@log_execution
def calc_vat(amount: float, vat_rate: float = 0.20) -> float:
  """Обчислює суму ПДВ."""
  if amount < 0:
    raise ValueError("Сума не може бути від'ємною")
  return amount * vat_rate

result = calc_vat(100.0)
print(f"Результат: {result}")