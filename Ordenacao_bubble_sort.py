# Lista original
lista = [29, -15, 45, -11, -33, 6, -43, 12, -40, 38, -8, -16, 30, -32, 46]

# Cria a funcao bubble sort passando a lista e o tamanho por parametro
def bubble_sort(lista, tam):
   troca = True
   while troca == True:
       troca = False
       for i in range(tam-1):
           if lista[i] > lista[i+1]:
               lista[i], lista[i+1] = lista[i+1], lista[i]
               troca = True
   return lista

# Ordenando a lista usando o Bubble Sort
lista_ordenada = bubble_sort(lista, 15)

# Exibindo a lista ordenada
print(lista_ordenada)
