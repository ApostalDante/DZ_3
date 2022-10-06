""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

number = int(input("Введите число: "))
result = []
while number > 0:
  result.append(number % 2)
  number = number // 2

print (* result, sep = "")