"""
LECTURE NOTES
MAP FILTER REDUCE

map()    – применяет функцию к каждому элементу
filter() – фильтрует элементы
reduce() – агрегирует элементы (из functools)

Обычно используется с lambda функциями.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map example
squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares)

# filter example
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce example
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum:", sum_all)