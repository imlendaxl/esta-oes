print('estamos no ano de 2023')
dia = int(input('digite um dia\n'))
mes = int(input('digite o mês\n '))

def estaçaodoano(dia, mes):
    if mes in (1, 2):
        return 'VERAO'
    elif mes == 3:
        if dia < 20:
            return 'VERAO'
        else:
            return 'OUTONO'
    elif mes in (4, 5):
        return 'OUTONO'
    elif mes == 6:
        if dia < 21:
            return 'OUTONO'
        else:
            return 'INVERNO'
    elif mes in (7, 8):
        return 'INVERNO'
    elif mes == 9:
        if dia < 23:
            return 'INVERNO'
        else:
            return 'PRIMAVERA'
    elif mes in (10, 11):
        return 'PRIMAVERA'
    elif mes == 12:
        if dia < 22:
            return 'PRIMAVERA'
        else:
            return 'VERAO'

resultado = estaçaodoano(dia, mes)
print(resultado)