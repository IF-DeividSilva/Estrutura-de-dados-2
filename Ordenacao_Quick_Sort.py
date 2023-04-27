def quick_sort(lista):
        
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menor = [x for x in lista[1:] if x <= pivo]
        maior = [x for x in lista[1:] if x > pivo]
        return quick_sort(menor) + [pivo] + quick_sort(maior)

lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8, -16, 30, -32, 46]
listaOrdenada = quick_sort(lista)
print(listaOrdenada)
