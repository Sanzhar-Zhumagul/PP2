def square(number):
    return number ** 2


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


if __name__ == "__main__":
    print(square(4))
    print(get_full_name("John", "Doe"))