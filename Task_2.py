#Функция бинарного поиска №1
def binary_search (array, searched_element):
    left = 0
    right = len(array)-1
    while left <= right:
        middle = (left + right) // 2
        if searched_element == array[middle]:
            return middle
        else:
            if searched_element > array[middle]:
                left = middle + 1
            else:
                right = middle - 1
    return None

#Вызываем модуль генератора случайных чисел
from random import randint

#Вводим число элементов списка, исключаем ошибку ввода дробного числа
try:
    n = int(input ("Введите целое положительное число:    "))
except ValueError:
    print ("Необходимо ввести целое число, нельзя вводить дробные")

#Генерирум массив случайных чисел
array_1 = []
for i in range(n):
    array_1.append(randint(1,250))
array_1.sort()
print (array_1)

#Вводим число, которое необходимо проверить
k = int(input ("Введите положительное число:    "))

#Вызываем функцию
a = binary_search(array_1, k)
print(a)

if a != None:
    print ("Число в списке под номером:", a+1)
else:
    print("Введенное число отсутствует в списке")