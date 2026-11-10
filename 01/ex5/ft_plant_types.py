class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name = name.casefold().capitalize()
        if height < 0 or curr_age < 0:
            print('Values cannot be negative')
            return
        self._height = round(height, 1)
        self._curr_age = curr_age
        print(f'Created: {self._name.capitalize()}: ', end='')
        print(f'{self._height}cm, {self._curr_age} day(s) old\n')

    def show(self) -> 'Plant':
        print(f'{self._name.capitalize()}: ', end="")
        print(f'{self._height}cm, {self._curr_age} day(s) old')
        return self

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


class Flower(Plant):
    def __init__(self, name: str, height: int,
                 curr_age: int, color: str) -> None:
        super().__init__(name, height, curr_age)
        self._color = color.casefold()
        self._bloom_state = f'{self._name} as not bloomed yet'

    def show(self) -> 'Flower':
        super().show()
        print(f'Color: {self._color}')
        print(f'{self._bloom_state}')
        return self

    def bloom(self) -> 'Flower':
        self._bloom_state = f'{self._name} is blooming beautifully!'
        print(f'[asking the {self._name.casefold()} to bloom]')
        return self


class Tree(Plant):
    def __init__(self, name: str, height: int, curr_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, curr_age)
        self._trunk_diameter = round(trunk_diameter, 1)

    def show(self) -> 'Tree':
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter}cm')
        return self

    def produce_shade(self) -> 'Tree':
        print(f'[asking the {self._name.casefold()} to produce shade]')
        print(f'Tree {self._name} now produces ', end='')
        print(f'a shade of {self._height}cm long ', end='')
        print(f'and {self._trunk_diameter}cm wide.')
        return self


class Vegetable(Plant):
    def __init__(self, name: str, height: int, curr_age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, curr_age)
        self._harvest_season = harvest_season.casefold().capitalize()
        self._nutritional_value = nutritional_value


if __name__ == "__main__":
    print('=== Garden Plant Types ===\n')
    h0 = 3
    p1 = Flower('rose', h0, 1, 'white')
    p1.set_age(3)
    p1.set_height(-1)
    p1.bloom().show()
    print('\n==Tree')
    t2 = Tree('Oak', 200, 365, 20)
    t2.produce_shade()
