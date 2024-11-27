def merge_sort(array, left, right):
    if left >= right:
        return array
    else:
        middle = (left + right)//2
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge (array, left, right, middle)

def merge (array, left_index, right_index, middle_index):
    left_array = array[left_index:middle_index+1] #Левый массив (С первого до центрального элемента)
    right_array = array[middle_index+1:right_index+1] #Правый массив (С центрального до правого элемента)
    i = 0 #Индекс левого массива
    j = 0 #Индекс правого массива
    k = left_index #Индекс отсортированного массива
    
    #Сравниваем элементы двух массивов
    while (i < len (left_array)) and (j < len (right_array)):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else:
            array[k] = right_array[j]
            j = j + 1
        k = k + 1
    
    #Когда один массив оказался пустым, необходимо в отсорированный массив добавить элементы из оставшегося
    while i < len (left_array):
        array[k] = left_array[i]
        i = i + 1
        k = k + 1
    while j < len (right_array):
        array[k] = right_array[j]
        j = j + 1
        k = k + 1