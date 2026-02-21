class Animal:
    def speak(self):
        print("Some sound")


class Cat(Animal):
    def speak(self):
        print("Meow")


if __name__ == "__main__":
    animal = Animal()
    cat = Cat()

    animal.speak()
    cat.speak()