def ft_water_reminder() -> None:
    if int(input('Days since last watering: ')) > 4:
        print('Water the plants!')
    else:
        print('Plants are fine')
