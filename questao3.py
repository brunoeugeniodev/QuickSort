# Condição de Parada Mal Definida

# O trecho if (left < j - 1) verifica se left é menor que 
# j - 1, e if (j + 1 < right) verifica se j + 1 é menor que right.

# No entanto, se j for igual a left ou right, pode ocorrer uma 
# chamada recursiva desnecessária ou até mesmo um loop infinito em casos extremos.

# Problemas com Subvetores Pequenos

# Se array tiver apenas um elemento, partition pode retornar left, 
# levando a chamadas recursivas erradas.

# Se array tiver dois elementos e o pivô não for corretamente 
# escolhido, a ordenação pode falhar.

# Falta de Tratamento para Casos Específicos

# Caso o vetor já esteja ordenado, pode acontecer de partition 
# escolher um pivô inadequado e realizar trocas desnecessárias.

# O código não verifica explicitamente se o vetor tem apenas um 
# elemento, o que poderia otimizar a execução.

def qsrt(array, left, right):
    if left >= right:  # Condição de parada correta
        return

    j = partition(array, left, right)

    # Garantindo que a divisão continue apenas quando há pelo menos dois elementos na partição
    if left < j:
        qsrt(array, left, j - 1)
    if j + 1 < right:
        qsrt(array, j + 1, right)
