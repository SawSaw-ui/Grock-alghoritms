"""

https://drive.google.com/file/d/1nFQGc_rjPUahinX_MtI87Zt6RqJRmfsq/view?usp=sharing

Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

"""

x = int(input('Введите номер буквы алфавита: '))

x = x + ord('a') - 1
y = chr(x)

print(f'Буква: {y}')
