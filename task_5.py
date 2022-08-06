# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма. Например, прибыль — выручка
# больше издержек, или убыток — издержки больше выручки. Выведите
# соответствующее сообщение.

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
        print(f'Congratulations! You profit is {my_rev - my_cost} cu!')
    elif my_rev < my_cost:
        print(f'Sorry, You losses is {my_cost - my_rev} cu')
    else:
        print(f'Pay attention, you profit is null!')
    my_rep = input(f'\nTry again? Input "n" for exit: ')
    if my_rep == 'n':
        my_rep = False
    else:
        my_rep = True
