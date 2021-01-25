"""

Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером
32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме:
по десять пар "код-символ" в каждой строке.

https://drive.google.com/file/d/1itcz4xlZ7WBH-zAQuY4-UHXQ8J3IQ1Uq/view?usp=sharing

"""

for i in range(32, 127, 10):
    for char in range(i, i+10):
        print(f"{char:2x} {chr(char):<4}", end="")
    print()
