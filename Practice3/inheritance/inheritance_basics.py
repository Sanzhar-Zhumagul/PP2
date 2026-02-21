class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    pass


if __name__ == "__main__":
    dog = Dog()
    dog.speak()