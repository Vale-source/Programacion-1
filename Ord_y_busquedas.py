def BubbleSort(lst):
    n = len(lst)

    for i in range(n-1):       
        for j in range(n-1-i): 
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def SelectionSort(lst):
    for i in range(len(lst) - 1):
        minimum = i 
        for j in range(i + 1, len(lst)): 
            if lst[j] < lst[minimum]:
                minimum = j
        if minimum != i:
            lst[minimum], lst[i] = lst[i], lst[minimum]
    return lst

def InsertionSort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >=0 and temp < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

def InsertionSort_for_len_words(lst): # Funcion creada para ordenar palabras por su longitud
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >=0 and len(temp) < len(lst[j]) :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

def MergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        sub_array1 = lst[:mid]
        sub_array2 = lst[mid:]

        MergeSort(sub_array1)
        MergeSort(sub_array2)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                lst[k] = sub_array1[i]
                i += 1
            else:
                lst[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            lst[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            lst[k] = sub_array2[j]
            j += 1
            k += 1
    return lst

def linear_search(lst,element): # Retorna el indice
    for variable in range(len(lst)):
        if (lst[variable] == element):
            return variable
    return False # Hacer un condicional en el codigo main por si el numero no esta en la lista

def binary_search(lst, target): # Retorna el indice
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = lst[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1

    return False # Hacer un condicional en el codigo main por si el numero no esta en la lista

def CountSort(lst):
    max_val = max(lst)
    min_val = min(lst)
    range_size = max_val - min_val + 1

    output = [0] * len(lst)
    count = [0] * range_size

    for i in lst:
        count[i - min_val] += 1
    
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    for i in range(len(lst) - 1, -1, -1):
        output[count[lst[i] - min_val] - 1] = lst[i]
        count[lst[i] - min_val] -= 1

    return output


