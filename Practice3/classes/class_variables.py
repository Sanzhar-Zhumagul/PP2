class Dog:
    species = "Canis familiaris"  # Переменная класса

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    dog1 = Dog("Buddy")
    dog2 = Dog("Max")

    print(dog1.name, dog1.species)
    print(dog2.name, dog2.species)