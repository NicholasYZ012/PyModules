class Plant:
    def __init__(self, name: str, height: float, curr_age: int) -> None:
        self._name = name.casefold().capitalize()
        if height < 0 or curr_age < 0:
            print('Values cannot be negative')
            return
        self._height = round(height, 1)
        self._curr_age = curr_age
        self._stats = self._Stats()
        print('Created: ', end='')
        self.show()

    def show(self) -> 'Plant':
        print(f'{self._name.capitalize()}: ', end="")
        print(f'{self._height}cm, {self._curr_age} day(s) old')
        self._stats._show_calls += 1
        return self

    def age(self) -> 'Plant':
        self._curr_age += 1
        self._stats._age_calls += 1
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
            self._curr_age += 1
        self._stats._grow_calls += 1
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

    @staticmethod
    def check_year_old(time: int) -> bool:
        if time > 365:
            return True
        return False

    @classmethod
    def create_anon(cls) -> 'Plant':
        return cls("Unknown plant", 0, 0)

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f'Stats: {self._grow_calls} grow', end=' ')
            print(f'{self._age_calls} age', end=' ')
            print(f'{self._show_calls} show')


class Flower(Plant):
    def __init__(self, name: str, height: int,
                curr_age: int, color: str) -> None:
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
    def __init__(self, name: str, height: int, curr_age: int,
                 trunk_diameter: float) -> None:
        self._trunk_diameter = round(trunk_diameter, 1)
        super().__init__(name, height, curr_age)

    def show(self) -> 'Tree':
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter}cm\n')
        return self

    def produce_shade(self) -> 'Tree':
        self._stats._shade_calls += 1
        print(f'[asking the {self._name.casefold()} to produce shade]')
        print(f'Tree {self._name} now produces ', end='')
        print(f'a shade of {self._height}cm long ', end='')
        print(f'and {self._trunk_diameter}cm wide.\n')
        return self

    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f'{self._shade_calls} shade')


class Vegetable(Plant):
    def __init__(self, name: str, height: int, curr_age: int,
                 harvest_season: str) -> None:
        self._harvest_season = harvest_season.casefold().capitalize()
        self._nutritional_value = 0
        super().__init__(name, height, curr_age)

    def show(self) -> 'Vegetable':
        super().show()
        print(f'Harvest season: {self._harvest_season}')
        print(f'Nutritional value: {self._nutritional_value}\n')
        return self

    def age(self) -> 'Vegetable':
        super().age()
        self._nutritional_value += 1
        return self

    def grow(self, days: int) -> 'Vegetable':
        super().grow(days)
        return self


class Seed(Flower):
    def __init__(self, name: str, height: int,
                curr_age: int, color: str) -> None:
        self._ori_age = curr_age
        self._seed_count = 0
        super().__init__(name, height, curr_age, color)

    def show(self) -> 'Seed':
        super().show()
        print(f'Seeds: {self._seed_count}')
        return self

    def bloom(self) -> 'Seed':
        super().bloom()
        self._seed_count = self._ori_age - self._curr_age


def disp_stats(plant: Plant) -> None:
    print(f'[statistics for {plant._name}]')
    plant._stats.display()


if __name__ == "__main__":
    print('=== Garden Plant Types ===\n')
    v1 = Vegetable("tomato", 30, 600, 'autumn')
    t1 = Tree('Mango', 100, 30, 50)
    f1 = Flower('Rose', 3, 3, 'white')
    v1.grow(600)
    t1.produce_shade()
    disp_stats(t1)
    disp_stats(v1)

