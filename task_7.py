# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10%
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное число —
# номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

my_rep = True
while my_rep:
    my_day = 1
    my_a = input('Input the first day result: ')
    my_ans = False
    while not my_ans:
        try:
            my_a = float(my_a)
            my_ans = True
        except ValueError:
            my_a = input(f'"{my_a}" is not a number! Try again: ')
    my_b = input('Input the wanted result: ')
    my_ans = False
    while not my_ans:
        try:
            my_b = float(my_b)
            my_ans = True
        except ValueError:
            my_b = input(f'"{my_b}" is not a number! Try again: ')
    while my_b > my_a:
        my_day += 1
        my_a += my_a / 10
         # print(f'{my_day} day - {my_a}')
    print(f'\nAnswer: {my_day} day')
    my_rep = input(f'\nTry again? Input "n" for exit: ')
    if my_rep == 'n':
        my_rep = False
    else:
        my_rep = True
