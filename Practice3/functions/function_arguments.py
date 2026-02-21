# Позиционные аргументы
def add(a, b):
    return a + b

# Именованные аргументы
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

if __name__ == "__main__":
    print(add(5, 3))
    introduce(age=25, name="Bob")