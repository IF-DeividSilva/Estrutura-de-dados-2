
def insertion_sort(lista, tam):
    for i in range(tam):
        auxy = lista[i]
        j = i-1
        while (j >= 0) and (auxy < lista[j]):
            lista[j+1] = lista[j]
            j = j-1
            lista[j+1] = auxy
    return lista    
    
lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8, -16, 30, -32, 46]
tamLista = len(lista)
listaOrdenada = insertion_sort(lista, tamLista)
print(listaOrdenada)
