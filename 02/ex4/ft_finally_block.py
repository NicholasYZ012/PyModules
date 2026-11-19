class GardenError(Exception):
    def __init__(self, *args: str) -> None:
        super().__init__(*args)


class PlantError(GardenError):
    def __init__(self, *args: str) -> None:
        super().__init__(*args)


def water_plant(plant_name: str) -> None:
    print(f'Watering {plant_name}: ', end='')
    if plant_name[0].isupper():
        print('OK')
    else:
        raise PlantError('Invalid plant name')


def test_watering_system() -> None:
    valid = ('Sunchoke', 'Oca', 'cucamelon')
    print('Opening watering system...')
    try:
        for veg in valid:
            water_plant(veg)
    except PlantError as e:
        print(f'Caught {PlantError.__name__}: {e}: {veg}')
        print('Ending tests and returning to main')
        return
    finally:
        print('Closing watering system')


if __name__ == '__main__':
    test_watering_system()
