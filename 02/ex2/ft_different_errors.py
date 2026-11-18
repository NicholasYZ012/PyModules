def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abs')
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open('troll')
    elif operation_number == 3:
        'abs' + 3
    print(f'Operation number = {operation_number}')


def test_error_types() -> None:
    i = 0
    while i < 6:
        try:
            garden_operations(i)
        except ValueError:
            print('Caught ValueError')
            print('Value passed into function is not the '
                  'expected type')
        except ZeroDivisionError:
            print('Caught ZeroDivisionError')
            print('Program tried to divide by 0')
        except FileNotFoundError:
            print('Caught FileNotFoundError')
            print('Program tried to open a file that '
                  'doesn\'t exist')
        except TypeError:
            print('Caught TypeError')
            print('Program tried to run operations on '
                  'incompatible types')
        i += 1
        print('Moving on...\n')


if __name__ == '__main__':
    test_error_types()
