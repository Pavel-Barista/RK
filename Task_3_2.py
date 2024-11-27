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
    array_1.append(randint(1,1000))
print (array_1)

print(selection_sort(array_1))