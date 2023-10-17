#comentario bryan

print('estamos no ano de 2023')
dia = int(input('digite um dia\n'))
mes = int(input('digite o mês\n '))

def seasons(dia, mes):
    if mes in (1, 2):
        return 'summer'
    elif mes == 3:
        if dia < 20:
            return 'summer'
        else:
            return 'fall'
    elif mes in (4, 5):
        return 'fall'
    elif mes == 6:
        if dia < 21:
            return 'fall'
        else:
            return 'winter'
    elif mes in (7, 8):
        return 'winter'
    elif mes == 9:
        if dia < 23:
            return 'winter'
        else:
            return 'spring'
    elif mes in (10, 11):
        return 'spring'
    elif mes == 12:
        if dia < 22:
            return 'spring'
        else:
            return 'summer'

resultado = seasons(dia, mes)
print(resultado)
