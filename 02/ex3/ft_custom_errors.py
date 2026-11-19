class GardenError(Exception):
    def __init__(self, msg: str) -> None:
        self.__str__ = msg


class PlantError(GardenError):
    def __init__(self, msg: str) -> None:
        self.__str__ = msg


class WaterError(GardenError):
    def __init__(self, msg: str) -> None:
        self.__str__ = msg


def neglect_plants() -> None:
    print('Test catching PlantError')
    raise PlantError('The plants are wilting!')


def out_of_water() -> None:
    print('Test catching WaterError')
    raise WaterError('Not enough water in the tank!')


def garden_state() -> None:
    func = [neglect_plants, out_of_water]
    for f in func:
        try:
            f()
        except PlantError as e:
            print(f'Caught {PlantError.__name__}: {e}')
        except WaterError as e:
            print(f'Caught {WaterError.__name__}: {e}')
    print('')
    for g in func:
        try:
            print('Test catching GardenError')
            g()
        except GardenError as e:
            print(f'Caught {GardenError.__name__}: {e}')


if __name__ == '__main__':
    garden_state()
