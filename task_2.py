# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

my_time = input('Input time in seconds: ')
my_ask = False
while not my_ask:
    try:
        my_time = int(my_time)
        my_ask = True
    except ValueError:
        my_time = input(f'"{my_time}" is not a number! Try again: ')
my_sec = my_time % 60
my_time = my_time - my_sec
my_hour = my_time // 3600
my_min = int((my_time - my_hour * 3600) / 60)
print(f'{my_hour}:{my_min // 10}{my_min % 10}:{my_sec // 10}{my_sec % 10}')
