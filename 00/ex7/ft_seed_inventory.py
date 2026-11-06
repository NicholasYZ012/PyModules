def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    formatted_seed_type = seed_type.casefold().capitalize()
    if unit == 'packets':
        print(f'{formatted_seed_type} seeds: {quantity} packets available')
    elif unit == 'grams':
        print(f'{formatted_seed_type} seeds: {quantity} grams total')
    elif unit == 'area':
        print(f'{formatted_seed_type} seeds: covers {quantity} square meters')
    else:
        print('Unknown unit type')
