# Lista original
lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8,  -16, 30, -32, 46]

# Cria a funcao selection sort passando a lista e o tamanho por parametro
def selection_sort(lista,tam):
    for i in range (tam):
        menor = i
        
        for aux in range (i+1, tam): 
            if lista[aux] < lista[menor]:
                menor = aux
        lista[menor], lista[i] = lista[i], lista[menor]
        
    return lista

tamLista = len(lista)
listaOrdenada = selection_sort(lista, 15)
print(listaOrdenada)