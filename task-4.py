import random
import timeit

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Генерація даних
def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, 1000000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))

# Порівняння часу виконання
sizes = [1000, 5000, 10000]
for size in sizes:
    data = generate_data(size, "random")
    print(f"Розмір масиву: {size}")
    print("Вставками:", timeit.timeit(lambda: insertion_sort(data.copy()), number=1))
    print("Злиттям:", timeit.timeit(lambda: merge_sort(data.copy()), number=1))
    print("Timsort (sorted):", timeit.timeit(lambda: sorted(data.copy()), number=1))
