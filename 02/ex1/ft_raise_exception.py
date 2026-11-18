class HighTemp(Exception):
    pass


class LowTemp(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp >= 0 and temp <= 40:
        return temp
    elif temp > 40:
        raise HighTemp
    raise LowTemp


def test_temperature() -> None:
    list = ['25', 'abc', '100', '-50']
    for test in list:
        print(f'Input data is {test}')
        try:
            print(f'Temperature is {input_temperature(test)}°C')
        except ValueError:
            print("Invalid input")
        except HighTemp:
            print(f'{test} is too hot for plants')
        except LowTemp:
            print(f'{test} is too cold for plants')
        print('')


if __name__ == "__main__":
    test_temperature()
