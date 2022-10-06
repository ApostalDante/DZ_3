""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

number_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(number_list) + 1) // 2):
  result_list.append(number_list[i] * number_list[len(number_list) -1 -i])
print (result_list)