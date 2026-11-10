class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name = name.casefold().capitalize()
        if height < 0 or curr_age < 0:
            print('Values cannot be negative')
            return
        self._height = height
        self._curr_age = curr_age
        print(f'Created: {self._name.capitalize()}: ', end="")
        print(f'{self._height}cm, {self._curr_age} day(s) old\n')

    def show(self) -> None:
        print(f'{self._name.capitalize()}: ', end="")
        print(f'{self._height}cm, {self._curr_age} day(s) old')

    def age(self) -> None:
        self._curr_age += 1

    def grow(self, days: int) -> float:
        tm = ((22 / 7) * (self._curr_age * self._height)) % 30
        k = self._height / self._curr_age
        if k >= 1:
            k = (22 / 7) * (10 ** self._curr_age) * k % 10 / 15
        elif k == 0:
            k = (22 / 7) * (10 ** self._curr_age) % 10 / 10

        def f(t: int) -> float:
            result: float = 1 + 1 / (2.71818 ** (k * (t - tm)))
            return result
        for n in range(days):
            t0 = self._curr_age
            h0 = self._height
            h1 = h0 * f(t0) / f(t0 + 1)
            self._height = round(h1, 1)
            self.age()
            print(f'=== Day {n + 1} ===')
            self.show()
        return self._height

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f'{self._name}: Error, height can\'t be negative')
            print('Height update rejected\n')
        else:
            self._height = new_height
            print(f'Height updated: {self._height}cm\n')

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f'{self._name}: Error, age can\'t be negative')
            print('Age update rejected\n')
        else:
            self._curr_age = new_age
            print(f'Age updated: {self._curr_age} days\n')

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._curr_age


if __name__ == "__main__":
    print('=== Plant Factory Output ===\n')
    h0 = 3
    p1 = Plant('rose', h0, 1)
    p1.set_age(3)
    p1.set_height(-1)
