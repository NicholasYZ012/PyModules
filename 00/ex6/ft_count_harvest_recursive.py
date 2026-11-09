def putday(num: int, max: int) -> None:
    if num <= max:
        print(f'Day {num}')
        putday(num + 1, max)


def ft_count_harvest_recursive() -> None:
    days = int(input('Days until harvest: '))
    putday(1, days)
    print('Harvest time!')
