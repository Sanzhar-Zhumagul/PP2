class Flyer:
    def fly(self):
        print("Flying...")


class Swimmer:
    def swim(self):
        print("Swimming...")


class Duck(Flyer, Swimmer):
    pass


if __name__ == "__main__":
    duck = Duck()
    duck.fly()
    duck.swim()