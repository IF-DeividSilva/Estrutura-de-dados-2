import random 
import time
import sys
import os

#funcao para gerar o vetor 
def geraVetor(tam, modo):
    if modo == 'c':
        # gera um vetor crescente
        return list(range(1, tam+1))
    elif modo == 'd':
        # gera um vetor decrescente
        return list(range(tam, 0, -1))
    elif modo == 'r':
        # gera um vetor aleatorio
        return [random.randint(0, 32000) for _ in  range(tam)]
    
#funcao para ordenar (insertion)
def insertionSort(lista):
    # variavel para contar o numero de comparacoes
    comparacoes = 0
    # variavel para contar o tempo de execucao
    inicio = time.time()
    for i in range(1, len(lista)):
        # variavel para guardar o valor a ser inserido
        chave = lista[i]
        # variavel para guardar a posicao do elemento anterior
        j = i-1
        while j >= 0 and chave < lista[j]:
            # troca os elementos de posicao
            lista[j+1] = lista[j]
            j = j-1
            comparacoes += 1
        # insere o elemento na posicao correta        
        lista[j+1] = chave
        comparacoes += 1    
    fim = time.time()
    # calcula o tempo de execucao
    tempo = int((fim - inicio) * 1000)    
    return (lista, comparacoes, tempo)

#funcao para ordenar (merge)
def mergeSort(lista):
    comparacoes1 = 0
    inicio = time.time()

    if len(lista) > 1:
        # divide a lista em duas partes
        meio = len(lista) // 2
        esq = lista[:meio]
        dir = lista[meio:]
        # Chama a função mergeSort recursivamente para ordenar a sublista esquerda
        esq, esq_comp, _ = mergeSort(esq)
        # Chama a função mergeSort recursivamente para ordenar a sublista direita
        dir, dir_comp, _ = mergeSort(dir)

        comparacoes1 += esq_comp + dir_comp

        i = 0
        j = 0 
        k = 0

        while i < len(esq) and j < len(dir):
            comparacoes1 += 1
            # ordena os elementos
            if esq[i] < dir[j]:
                # insere o elemento na lista
                lista[k] = esq[i]
                i += 1
            else:
                # insere o elemento na lista
                lista[k] = dir[j]
                j += 1
            k += 1

        while i < len(esq):
            # insere o elemento na lista
            lista[k] = esq[i]
            i += 1
            k += 1
        
        while j < len(dir):
            # insere o elemento na lista
            lista[k] = dir[j]
            j += 1
            k += 1

    fim = time.time()
    tempo = int((fim - inicio) * 1000)

    return lista, comparacoes1, tempo

#funcao para ordenar (bubble)
def bubbleSort(lista):
    inicio = time.time()
    comparacoes2 = -1
    n = len(lista)
    # percorre a lista
    for i in range(n):
        comparacoes2 += 1
        # percorre a lista 
        for j in range(n - i - 1):
            # compara os elementos
            if lista[j] > lista[j + 1]:
                # troca os elementos de posicao
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
    fim = time.time()
    tempo = int((fim - inicio) * 1000)
    return (lista, comparacoes2, tempo)

#funcao para ordenar (selection)
def selectionSort(lista):
    inicio = time.time()
    comparacoes0 = 0
    # percorre a lista
    for i in range(len(lista)-1, 0, -1):
        # variavel para guardar a posicao do maior elemento
        maior = 0
        # percorre a lista
        for j in range(1, i+1):
            comparacoes0 += 1
            # compara os elementos
            if lista[j] > lista[maior]:
                # guarda a posicao do maior elemento
                maior = j
        # troca os elementos de posicao       
        lista[i], lista[maior] = lista[maior], lista[i]
    fim = time.time()
    tempo = int((fim - inicio) * 1000)
    return (lista, comparacoes0, tempo)

#funcao para ordenar (quick)
def quickSort(lista):
    count = [0]*1
    inicio = time.time()
    # chama a funcao auxiliar
    quickSortHelper(lista, 0, len(lista)-1, count)
    fim = time.time()
    tempo = int((fim - inicio) * 1000)    
    return (lista, count[0], tempo)

def quickSortHelper(lista, primeiro, ultimo, count):
    # chama a funcao particao
    if primeiro < ultimo:
        # chama a funcao particao
        splitpoint = particao(lista, primeiro, ultimo, count)
        quickSortHelper(lista, primeiro, splitpoint-1, count)
        quickSortHelper(lista, splitpoint+1, ultimo, count)

def particao(array, first, last, count):
    pivo = array[first]
    left = first+1
    right = last
    # variavel para controlar o loop
    done = False
    # percorre a lista
    while not done:
        while left <= right and array[left] <= pivo:
            left += 1
            count[0] += 1
        while array[right] >= pivo and right >= left:
            right -= 1
            count[0] += 1
        if right < left:
            done = True
            count[0] += 1
        else:
            # troca os elementos de posicao
            array[left], array[right] = array[right], array[left]
    # troca os elementos de posicao
    array[first], array[right] = array[right], array[first]
    return right

#funcao para ordenar (heap)
def maxHeapify(lista, i, heapSize, comparacoes):
    left  = 2*i+1
    right = 2*i+2
    largest = i
    # compara os elementos
    if(left <= (heapSize-1)) and (lista[left] > lista[i]):
        # guarda a posicao do maior elemento 
        largest = left
    # compara os elementos    
    if (right <= (heapSize-1)) and (lista[right] > lista[largest]):
        # guarda a posicao do maior elemento
        largest = right
    if i != largest:
        # troca os elementos de posicao
        lista[i], lista[largest] = lista[largest], lista[i]
        comparacoes += 1
        maxHeapify(lista, largest, heapSize-1, comparacoes)

    return comparacoes

def buildMaxHeap(lista, heapSize, comparacoes): #ok
    idxs = range(len(lista)//2, -1, -1)
    for index in idxs:
        comparacoes = maxHeapify(lista, index, heapSize, comparacoes)

    return comparacoes
#funcao para ordenar (heap)
def heapSort(lista):
    inicio = time.time()
    heapSize = len(lista)
    comparacoes = 0
    comparacoes = buildMaxHeap(lista, heapSize, comparacoes)
    idxs = range(len(lista)-1, 0, -1)
    
    for index in idxs:
        # troca os elementos de posicao
        lista[0], lista[index] = lista[index], lista[0]
        comparacoes += 1
        heapSize = heapSize - 1
        comparacoes = maxHeapify(lista, 0, heapSize, comparacoes)
    fim = time.time()
    tempo = int((fim - inicio) * 1000)  
    return (lista, comparacoes, tempo)

#arg c argv[1] argv[2]
sys.setrecursionlimit(10001)
arquivo_input = sys.argv[1]
arquivo_output = sys.argv[2]

#abre o arquivo
with open(arquivo_input, 'r') as f:
    #verifica se o arquivo esta vazio
    if os.stat(arquivo_input).st_size == True:
        with open(arquivo_output, 'w') as f:
            f.write(f"Arquivo Vazio!")
        exit()
    tam = int(f.readline().strip())
    modo = f.readline().strip()
    #verifica se o arquivo eh valido
    if modo != 'c':
        if modo != 'd':
            if modo != 'r':
                with open(arquivo_output, 'w') as f:
                    f.write(f"Arquivo Invalido!")
                exit()
    lista = geraVetor(tam, modo)
#abre o arquivo de saida e escreve os resultados
with open(arquivo_output, 'w') as f:
    ListaOrdenada, comp, tempo = insertionSort(lista)
    f.write(f"InsertionSort: {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
    ListaOrdenada, comp, tempo = selectionSort(lista)
    f.write(f"SelectionSort: {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
    ListaOrdenada, comp, tempo = bubbleSort(lista)
    f.write(f"BubbleSort:    {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
    ListaOrdenada, comp, tempo = mergeSort(lista)
    f.write(f"MergeSort:     {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
    ListaOrdenada, comp, tempo = quickSort(lista)
    f.write(f"QuickSort:     {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
    ListaOrdenada, comp, tempo = heapSort(lista)
    f.write(f"HeapSort:      {ListaOrdenada} comp: {comp} temp: {tempo}ms\n")
#fecha o arquivo
f.close()
