"""
Изучаем операторы.
Название файла '08.операторы.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-03
"""

# вводим данные
a = int(input('Пожалуйста, введите целое значение переменной а=: '))
print("a = ", a)
b = int(input('Пожалуйста, введите целое значение переменной b=: '))
print("b = ", b)
c = int(input('Пожалуйста, введите целое значение переменной c=: '))
print("c = ", c)

# Выводим примеры с этими данными
result = (a + b)
print("Результат сложения двух переменных a + b = ", result)

a += b
print("В выражении a += b мы переопределяем значение переменной а = a + b, после чего а=", a)

print("Учитывая что теперь a = ", a)
a *= c
print("Выражение a *= c, переопределяет значение переменной а = а * с, после чего а=", a)

print("Учитывая что теперь a = ", a)
a -= c
print("Выражение a -= c, переопределяет значение переменной а = а - с, после чего а=", a)

print("Учитывая что теперь a = ", a)
a /= c
print("Выражение a /= с, переопределяет значение переменной а = а / с, после чего а=", a)


flag1 = 4 > 1  # True
flag2 = 5 < 1  # False
flag3 = flag1 and flag2  # логическое умножение истина на ложь = False
flag4 = flag1 or flag2  # логическое сложение истина или ложь = True
flag5 = not flag1  # противопложное значение истины = False

# выводим полученные результаты
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)  # истина это истина = True
print(flag2 is not False)  # ложь это не ложь = False
