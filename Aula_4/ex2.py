from array import array

array = [22, 89, 125, 1, 855]

n = len (array)
for i in range (n):
    min_idx = i

    for j in range (i + 1 , n):
        if array [j] < array [min_idx]:

            min_idx = j
    array [i], array [min_idx] = array [min_idx], array[i]

print("Lista Original", array)
print("Lista Ordenada", array)
