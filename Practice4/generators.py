#.  __iter__()
#.  __next__()
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current
#.  Генераторная функция
def count_up_to(n):
    for i in range(1, n + 1):
        yield i
#.  Генераторные выражения
gen = (x * 2 for x in range(10))
#.  Ключевые функции модуля itertools
from itertools import count, cycle, repeat, chain, combinations
#.  yield from
def gen1():
    yield from range(5)
#.  Практические паттерны
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1
#.  send(), throw(), close()
def echo():
    while True:
        value = yield
        print(value)