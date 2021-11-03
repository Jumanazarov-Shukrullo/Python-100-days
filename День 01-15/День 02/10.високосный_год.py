"""
Если входной год является високосным, выведите True, иначе выведите False.
Название файла '10.високосный_год.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-03
"""

# вводим любой интерисующий нас год
year = int(input('Пожалуйста, введите год: '))
# Если код слишком длинный для записи в одну строку и его нелегко читать, вы можете использовать \ или (), чтобы разорвать строку


is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)  # производим вычисления


if is_leap == False:  # если значение переменной равно ЛОЖЬ то ..
    print('Год - не високосный')
else:
    print('Год - високосный')


