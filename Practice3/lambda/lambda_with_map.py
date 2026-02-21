numbers = [1, 2, 3, 4, 5]

# Использование lambda с map
squared = list(map(lambda x: x ** 2, numbers))

if __name__ == "__main__":
    print("Original:", numbers)
    print("Squared:", squared)