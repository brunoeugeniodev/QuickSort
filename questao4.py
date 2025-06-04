# Erro na Lógica de Troca

# O objetivo da separação é reorganizar os elementos de modo que os maiores
# fiquem à esquerda do pivô e os menores fiquem à direita.

# No entanto, a troca array[i], array[right] = array[right], array[i] simplesmente 
# move array[i] para a posição do pivô, sem garantir que os elementos menores 
# estejam agrupados corretamente.

# Pivô Mudando de Lugar Indevidamente

# Ao realizar a troca array[i] ↔ array[right], o pivô pode ser movido para 
# outra posição antes que todo o vetor seja particionado corretamente, 
# resultando em um estado inconsistente.

# Posicionamento Errado do Índice j

# O índice j não está sendo atualizado corretamente para refletir a posição 
# final do pivô após a separação.

# Comportamento Indevido para Subvetores Pequenos

# Se houver apenas dois elementos, a função pode não garantir que eles 
# fiquem ordenados corretamente.

def partition(array, left, right):
    pivot = array[right]  # Escolhe o último elemento como pivô
    i = left - 1  # Ponteiro para os elementos menores que o pivô

    for j in range(left, right):
        if array[j] >= pivot:  # Comparação ajustada para ordenação decrescente
            i += 1
            array[i], array[j] = array[j], array[i]  # Troca elementos

    array[i + 1], array[right] = array[right], array[i + 1]  # Coloca o pivô na posição correta
    return i + 1  # Retorna o índice final do pivô
