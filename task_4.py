# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

my_rep = True
while my_rep:
    my_ind = 1
    my_max = 0
    my_ask = False
    my_num = input('Input a number: ')
    while not my_ask:
        my_len = len(my_num)
        try:
            my_num = int(my_num)
            my_ask = True
        except ValueError:
            my_num = input(f'"{my_num}" is not a number! Try again: ')
    while my_ind <= my_len:
        my_dig = (my_num % (10 ** my_ind)) // 10 ** (my_ind - 1)
        if my_dig > my_max:
            my_max = my_dig
        my_ind += 1
    print(f'Maximum of {my_len} digits is {my_max}')
    my_rep = input('Try again? Input "n" for exit: ')
    if my_rep == 'n':
        my_rep = False
    else:
        my_rep = True
