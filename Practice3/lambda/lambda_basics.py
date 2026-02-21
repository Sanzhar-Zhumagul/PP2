# Обычная функция
def square(x):
    return x ** 2


# Lambda функция
square_lambda = lambda x: x ** 2


if __name__ == "__main__":
    print(square(5))
    print(square_lambda(5))