# Método de ordenamiento Burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Método de ordenamiento Por Selección
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11, 90, 5]
bubble_sort(arr)
print("Lista ordenada usando Burbuja:")
print(arr)

arr = [64, 25, 12, 22, 11, 90, 5]
selection_sort(arr)
print("Lista ordenada usando Por Selección:")
print(arr)