from collections import deque
import time
import random

def partition(array, inicio, fim):
    pivot = array[inicio]
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

def quick_sort_iterative(array):
    stack = deque()
    stack.append((0, len(array) - 1))

    while stack:
        inicio, fim = stack.pop()
        if inicio >= fim:
            continue

        pivot_index = partition(array, inicio, fim)
        stack.append((inicio, pivot_index - 1))
        stack.append((pivot_index + 1, fim))

def quick_sort_recursive(array, inicio, fim):
    if inicio >= fim:
        return

    pivot_index = partition(array, inicio, fim)
    quick_sort_recursive(array, inicio, pivot_index - 1)
    quick_sort_recursive(array, pivot_index + 1, fim)

# Função para testar e medir tempo de execução
def testar_quick_sort(tamanhos):
    resultados = []

    for tamanho in tamanhos:
        array = [random.randint(1, 10000) for _ in range(tamanho)]
        
        # Teste versão iterativa
        array_iterativo = array[:]
        inicio = time.time()
        quick_sort_iterative(array_iterativo)
        tempo_iterativo = time.time() - inicio
        
        # Teste versão recursiva
        array_recursivo = array[:]
        inicio = time.time()
        quick_sort_recursive(array_recursivo, 0, len(array) - 1)
        tempo_recursivo = time.time() - inicio

        resultados.append((tamanho, tempo_iterativo, tempo_recursivo))

    return resultados

# Executar testes
tamanhos = [1000, 5000, 10000, 50000]
resultados = testar_quick_sort(tamanhos)

# Exibir resultados em tabela
print("\nComparação entre versões iterativa e recursiva do Quick Sort\n")
print(f"{'Tamanho do Vetor':<20}{'Tempo Iterativo (s)':<20}{'Tempo Recursivo (s)':<20}")
for tamanho, tempo_iterativo, tempo_recursivo in resultados:
    print(f"{tamanho:<20}{tempo_iterativo:<20.6f}{tempo_recursivo:<20.6f}")

