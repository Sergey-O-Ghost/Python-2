# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

my_num = input('Input a number: ')
my_ask = False
while not my_ask:
    try:
        my_sum = int(my_num)
        my_ask = True
    except ValueError:
        my_num = input(f'"{my_num}" is not a number! Try again: ')
for my_ind in range(2,4):
    my_sum += int(my_num * my_ind)
print(f'{my_num} + {my_num * 2} + {my_num * 3} = {my_sum}')
