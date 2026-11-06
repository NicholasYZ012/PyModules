def ft_harvest_total():
    weight = 0
    n = 1
    while n <= 3:
        weight += int(input(f'Day {n} harvest: '))
        n += 1
    print(f'Total harvest: {weight}')
