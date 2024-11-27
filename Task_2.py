#Функция линейного поиска №5
def recursive_linear_search (array, i, searched_element):
    if i > len (array)-1:
        return None
    else:
        if array[i] == searched_element:
            return i
        else:
            return recursive_linear_search (array, i+1, searched_element)

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
a = recursive_linear_search(array_1, 0, k)
print(a)

if a != None:
    print ("Число в списке под номером:", a+1)
else:
    print("Введенное число отсутствует в списке")