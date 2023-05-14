def heapify(arr, n, i):
    # Essa função cria um heap máximo
    # na subárvore com raiz em índice i

    largest = i  # Inicializa o maior como raiz
    l = 2 * i + 1  # Esquerda = 2*i + 1
    r = 2 * i + 2  # Direita = 2*i + 2

    # Verifica se a subárvore da esquerda existe e se seu valor é maior que o nó raiz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Verifica se a subárvore da direita existe e se seu valor é maior que o nó raiz
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Troca o nó raiz se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Chama heapify recursivamente na subárvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai um por um os elementos do heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Exemplo de uso:
lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8, -16, 30, -32, 46]
heap_sort(lista)
print(lista)
