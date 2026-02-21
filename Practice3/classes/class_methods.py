class MathOperations:

    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


if __name__ == "__main__":
    print(MathOperations.add(3, 5))
    print(MathOperations.multiply(4, 6))