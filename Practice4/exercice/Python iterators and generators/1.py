def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i
for sq in generate_squares(5):
    print(sq)