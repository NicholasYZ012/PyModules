def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    list = ['25', 'abc']
    for test in list:
        try:
            print(f'Temperature is {input_temperature(test)}°C')
        except ValueError:
            print("Caught ValueError")
        print('I am still running!')


if __name__ == "__main__":
    test_temperature()
