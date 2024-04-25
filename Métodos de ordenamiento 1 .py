# Método de ordenamiento Burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Método de ordenamiento Por Inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Lista ordenada usando Burbuja:")
print(arr)

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Lista ordenada usando Por Inserción:")
print(arr)