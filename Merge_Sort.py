
def merge_sort(lista):
    #caso base
    if len(lista) <= 1:
        return lista

    #divide a lista no meio    
    meio = len(lista) // 2
    #chamada recursiva da funcao merg_sort a cada metadade
    inicio = merge_sort(lista[:meio])
    fim = merge_sort(lista[meio:])

    return merge(inicio, fim)

def merge( inicio, fim):
    aux=[]
    p1 = 0
    p2 = 0

    # ordena as duas metades no vetor aux
    while p1 < len(inicio) and p2 < len(fim):
        if inicio[p1] < fim[p2]:
            aux.append(inicio[p1])
            p1 = p1+1
        else:
            aux.append(fim[p2])
            p2 = p2+1    
    # adiciona os elementos que faltam em cada metade
    aux = aux + inicio[p1:]
    aux = aux + fim[p2:]   

    return aux     




lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8, -16, 30, -32, 46]
listaOrdenada = merge_sort(lista)
print(listaOrdenada)