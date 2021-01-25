"""

https://drive.google.com/file/d/1Npz0bhLP35dzRtF6Vn2JEuNPNyNSTnwh/view?usp=sharing

Сформировать из введенного числа обратное
по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

"""

num = int(input('Введите число: '))
m = 0
while num > 0:
    m = m * 10 + num % 10
    num = num // 10

print(f'Число в обратном порядке: {m}')
