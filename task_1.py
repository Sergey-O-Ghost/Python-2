# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

my_num_1  = 122
my_str_1 = 'Hello, Torvalds!'
my_ask = False
my_num_2 = input('Input a number: ')
while not my_ask:
    try:
        my_num_2 = int(my_num_2)
        my_ask = True
    except ValueError:
        my_num_2 = input(f'"{my_num_2}" is not a number! Try again: ')
my_str_2 = input('input a string: ')
print(f'\nMy variables:\n{my_num_1}\n{my_str_1}\n\nYou variables:\n{my_num_2}'
      f'\n{my_str_2}')
