#Функция линейного поиска №4
def sentinel_linear_search (array, searched_element):
    last = array[(len(array)-1)]
    array[(len(array)-1)] = searched_element
    i=0
    while array[i] != searched_element:
        i += 1
    array[(len(array)-1)] = last
    if i < (len(array)-1) or array[(len(array)-1)] == searched_element:
        print ("Число в списке под номером", i+1)
    else:
        print("Введенное число отсутствует в списке")

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
sentinel_linear_search(array_1, k)