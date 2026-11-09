class Plant:
    def __init__(self, name: str, height: float, curr_age: int):
        self.name = name
        self.height = height
        self.curr_age = curr_age

    def show(self):
        print(f'{self.name.capitalize()}: ', end="")
        print(f'{self.height}cm, {self.curr_age} day(s) old')

    def age(self):
        self.curr_age += 1

    def grow(self, days: int) -> float:
        tm = ((22 / 7) * (self.curr_age * self.height)) % 30
        k = self.height / self.curr_age
        if k >= 1:
            k = (22 / 7) * (10 ** self.curr_age) * k % 10 / 15
        elif k == 0:
            k = (22 / 7) * (10 ** self.curr_age) % 10 / 10

        def f(t: int) -> int:
            return 1 + 1 / (2.71818 ** (k * (t - tm)))
        for n in range(days):
            t0 = self.curr_age
            h0 = self.height
            h1 = h0 * f(t0) / f(t0 + 1)
            self.height = round(h1, 1)
            self.age()
            print(f'=== Day {n + 1} ===')
            self.show()
        return self.height


if __name__ == "__main__":
    print('=== Garden Plant Growth ===')
    h0 = 3
    p1 = Plant('tomato', h0, 3)
    p1.show()
    h1 = p1.grow(7)
    print(f'Growth this week: {h1 - h0}cm')
