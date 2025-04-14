from array import array

array = [9, 2, 6, 3, 8]

n = len(array)

for i in range (n):
    for j in range(0, n -i - 1):
        if array [j] > array [j +1]:
            array[j], array [j + 1] = array [j + 1], array [j]

print("lista original", array)
print("lista ordenada", array)
