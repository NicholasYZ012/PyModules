class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self.name = name.casefold().capitalize()
        self.height = height
        self.curr_age = curr_age

    def show(self) -> None:
        print(f'{self.name.capitalize()}: ', end="")
        print(f'{self.height}cm, {self.curr_age} day(s) old')

    def age(self) -> None:
        self.curr_age += 1

    def grow(self, days: int) -> float:
        tm = ((22 / 7) * (self.curr_age * self.height)) % 30
        k = self.height / self.curr_age
        if k >= 1:
            k = (22 / 7) * (10 ** self.curr_age) * k % 10 / 15
        elif k == 0:
            k = (22 / 7) * (10 ** self.curr_age) % 10 / 10

        def f(t: int) -> float:
            result: float = 1 + 1 / (2.71818 ** (k * (t - tm)))
            return result
        for n in range(days):
            t0 = self.curr_age
            h0 = self.height
            h1 = h0 * f(t0) / f(t0 + 1)
            self.height = round(h1, 1)
            self.age()
            print(f'=== Day {n + 1} ===')
            self.show()
        return self.height

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print('')
        else:
            self.height = new_height

    def set_age(self, new_age: int) -> None:
        self.curr_age = new_age

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.curr_age


if __name__ == "__main__":
    print('=== Plant Factory Output ===')
    h0 = 3
    p1 = Plant('tomato', h0, 3)
