# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

my_rep = True
while my_rep:
    my_ask = False
    my_rev = input('Input the revenue: ')
    while not my_ask:
        try:
            my_rev = float(my_rev)
            my_ask = True
        except ValueError:
            my_rev = input(f'"{my_rev}" is not a number! Try again: ')
    my_ask = False
    my_cost = input('Input the cost: ')
    while not my_ask:
        try:
            my_cost = float(my_cost)
            my_ask = True
        except ValueError:
            my_cost = input(f'"{my_cost}" is not a number! Try again: ')
    if my_rev > my_cost:
        my_ask = False
        my_num = input('Input the number of staff: ')
        while not my_ask:
            try:
                my_num = int(my_num)
                my_ask = True
            except ValueError:
                my_num = input(f'"{my_num}" is not a number! Try again: ')
        my_ppe = round((my_rev - my_cost) / my_num, 2)
        my_pa = int((my_rev - my_cost) * 100 // my_rev)
        print(f'Congratulations! You profit is {my_rev - my_cost} cu!\nYou '
              f'profitability is {my_pa}%\nProfit per employee is {my_ppe} cu'
              f'\n\n*cu - conventional unit')
    elif my_rev < my_cost:
        print(f'Sorry, You losses is {my_cost - my_rev} cu')
    else:
        print(f'Pay attention, you profit is null!')
    my_rep = input(f'\nTry again? Input "n" for exit: ')
    if my_rep == 'n':
        my_rep = False
    else:
        my_rep = True
