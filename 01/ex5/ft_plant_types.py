class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name = name.casefold().capitalize()
        if height < 0 or curr_age < 0:
            print('Values cannot be negative')
            return
        self._height = round(height, 1)
        self._curr_age = curr_age
        print('Created: ', end='')
        self.show()

    def show(self) -> 'Plant':
        print(f'{self._name.capitalize()}: ', end="")
        print(f'{self._height}cm, {self._curr_age} day(s) old')
        return self

    def age(self) -> 'Plant':
        self._curr_age += 1
        return self

    def grow(self, days: int) -> 'Plant':
        tm = ((22 / 7) * (self._curr_age * self._height)) % 30
        k = self._height / (self._curr_age + 1)
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
        return self

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f'{self._name}: Error, height can\'t be negative')
            print('Height update rejected\n')
        else:
            self._height = round(new_height, 1)
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
    def __init__(self, name: str, height: float, curr_age: int,
                 color: str) -> None:
        self._bloom_state = 'unbloom'
        self._color = color.casefold()
        super().__init__(name, height, curr_age)

    def show(self) -> 'Flower':
        super().show()
        print(f'Color: {self._color}')
        if self._bloom_state == 'unbloom':
            print(f'{self._name} has not bloomed yet\n')
        else:
            print(self._bloom_state)
        return self

    def bloom(self) -> 'Flower':
        self._bloom_state = f'{self._name} is blooming beautifully!\n'
        print(f'[asking the {self._name.casefold()} to bloom]')
        print(self._bloom_state)
        return self


class Tree(Plant):
    def __init__(self, name: str, height: float, curr_age: int,
                 trunk_diameter: float) -> None:
        self._trunk_diameter = round(trunk_diameter, 1)
        super().__init__(name, height, curr_age)

    def show(self) -> 'Tree':
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter}cm\n')
        return self

    def produce_shade(self) -> 'Tree':
        print(f'[asking the {self._name.casefold()} to produce shade]')
        print(f'Tree {self._name} now produces ', end='')
        print(f'a shade of {self._height}cm long ', end='')
        print(f'and {self._trunk_diameter}cm wide.\n')
        return self


class Vegetable(Plant):
    def __init__(self, name: str, height: float, curr_age: int,
                 harvest_season: str) -> None:
        self._harvest_season = harvest_season.casefold().capitalize()
        self._nutritional_value = 0
        super().__init__(name, height, curr_age)

    def show(self) -> 'Vegetable':
        super().show()
        print(f'Harvest season: {self._harvest_season}')
        print(f'Nutritional value: {self._nutritional_value}\n')
        return self

    def age(self) -> Vegetable:
        super().age()
        self._nutritional_value += 1
        return self

    def grow(self, days: int) -> Vegetable:
        super().grow(days)
        return self


if __name__ == "__main__":
    print('=== Garden Plant Types ===\n')
    v1 = Vegetable("tomato", 30, 600, 'autumn')
    t1 = Tree('Mango', 100, 30, 50)
    f1 = Flower('Rose', 3, 3, 'white')
    v1.grow(600)
    t1.produce_shade()
    f1.bloom()
    v1.show()
