"""
Задача 3
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""
def gen_fib(n):
    n1, n2 = 1, 1
    for i in range(1, n + 1):
        if i < 3:
            yield 1
        else:
            yield n1 + n2
            n1, n2 = n2, n1 + n2