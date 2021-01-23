"""
Схема:

https://drive.google.com/file/d/1oO5tLjpp542q4CpFf4fFjsHA4BGaJPL_/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.

"""

n = input("Введите трехзначное число: ")

n = int(n)

d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100

print("Сумма цифр числа:", d1 + d2 + d3)
print("Произведение цифр числа:", d1 * d2 * d3)

