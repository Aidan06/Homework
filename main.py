# task1
# a = int('введите первое число:')
# b = int('введите второе число:')

# if a <0 and b > 0:
#     print('оба числа отрицательные')
# elif a> -1 and b > -1:
#     print('оба числа положительные')

#  task 3
# Cгенерируйте и выведите на экран мозаичное и
# зображение гексагональной сетки, напоминающее 
# мелкоячеистую проволочную сетку.

for i in range(2, 15):
    if i % 2 == 0:
        for j in range (2, 15):
            print('/ \_', end ='')
        print('')

    else: 
        for i in range(2, 15):
            print('\_/ ', end = '')
        print('')


