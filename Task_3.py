#Функция "Сортировка выбором"
def selection_sort(array):
    for i in range (len(array)-1):
        the_smallest = i
        for j in range (i+1, len(array)):
            if array[j] < array [the_smallest]:
                the_smallest = j
        array[i], array[the_smallest] = array[the_smallest], array[i]
    return array