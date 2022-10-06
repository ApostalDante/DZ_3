""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

number_list = [1.1, 1.2, 3.1, 10.01]
min = 1
max = 0
for i in number_list:
  if (i - int(i)) > max:
    max = i - int(i)
  if (i - int(i)) < min:
    min = i - int(i)

print (round(max - min, 2))