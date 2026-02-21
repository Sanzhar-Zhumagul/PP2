numbers = [1, 2, 3, 4, 5, 6]

# Использование lambda с filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == "__main__":
    print("Original:", numbers)
    print("Even numbers:", even_numbers)