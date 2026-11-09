class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age} days old')


if __name__ == "__main__":
    plant1 = Plant('tomato', 3, 4)
    p2 = Plant('corn', 42, 69)
    p3 = Plant('wheat', 25, 30)
    print('=== Garden Plant Registry ===')
    plant1.show()
    p2.show()
    p3.show()
