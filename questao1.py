def partition(array, inicio, fim):
    pivot = array[inicio]  # Escolhe o primeiro elemento como pivô
    left = inicio + 1
    right = fim

    while True:
        while left <= right and array[left] >= pivot:
            left += 1
        while left <= right and array[right] < pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            break

    array[inicio], array[right] = array[right], array[inicio]
    return right

def quick_sort(array, inicio, fim):
    if inicio >= fim:
        return

    pivot_index = partition(array, inicio, fim)
    quick_sort(array, inicio, pivot_index - 1)
    quick_sort(array, pivot_index + 1, fim)

# Exemplo de uso
array = [10, 3, 8, 15, 6, 1, 9]
quick_sort(array, 0, len(array) - 1)
print("Array ordenado em ordem decrescente:", array)
