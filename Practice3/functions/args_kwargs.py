# *args — произвольное количество позиционных аргументов
def sum_all(*args):
    return sum(args)


# **kwargs — произвольное количество именованных аргументов
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print(sum_all(1, 2, 3, 4))
    print_info(name="Alice", age=30, city="New York")