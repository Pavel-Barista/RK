#Функция линейного поиска №2
def better_linear_search (array, searched_element):
    for i in range (len(array)):
        if searched_element == array[i]:
             return i+1
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
    array_1.append(randint(1,50))
array_1.sort()
print (array_1)

#Вводим число, которое необходимо проверить
k = int(input ("Введите положительное число:    "))

#Вызываем функцию
a = better_linear_search(array_1, k)
print(a)

if a != None:
    print ("Число в списке под номером:", a)
else:
    print("Введенное число отсутствует в списке")