""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

number = int(input("Введите число: "))

def get_fibonacci(number):
    fibonacci_numbers = []
    a, b = 1, 1
    for i in range(number):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (number + 1):
        fibonacci_numbers.insert(0, a)
        a, b = b, a - b
    return fibonacci_numbers

fibonacci_numbers = get_fibonacci(number)
print(get_fibonacci(number))
