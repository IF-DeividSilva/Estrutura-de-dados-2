import sys
import os
import re

class Heroi:
    def __init__(self):
        self.chave = None
        self.primeiroNome = None
        self.sobreNome = None
        self.nomeHeroi = None
        self.poder = None
        self.fraqueza = None
        self.cidade = None
        self.profissao = None

#construtor
class Heroi:
    def __init__(self, chave, primeiroNome, sobreNome, nomeHeroi, poder, fraqueza, cidade, profissao):
        self.chave = chave
        self.primeiroNome = primeiroNome
        self.sobreNome = sobreNome
        self.nomeHeroi = nomeHeroi
        self.poder = poder
        self.fraqueza = fraqueza
        self.cidade = cidade
        self.profissao = profissao

def insertionsort_crescente(herois):
    for i in range(1, len(herois)):
        chave_atual = herois[i]
        j = i - 1
        while j >= 0 and herois[j].chave > chave_atual.chave:
            herois[j + 1] = herois[j]
            j -= 1
        herois[j + 1] = chave_atual

def insertionsort_decrescente(herois):
    for i in range(1, len(herois)):
        chave_atual = herois[i]
        j = i - 1
        while j >= 0 and herois[j].chave < chave_atual.chave:
            herois[j + 1] = herois[j]
            j -= 1
        herois[j + 1] = chave_atual   

def quicksort_crescente(herois, inicio, fim):
    if inicio < fim:
        pivo = particionar(herois, inicio, fim)
        quicksort_crescente(herois, inicio, pivo - 1)
        quicksort_crescente(herois, pivo + 1, fim)

def quicksort_decrescente(herois, inicio, fim):
    if inicio < fim:
        pivo = particionar(herois, inicio, fim)
        quicksort_decrescente(herois, inicio, pivo - 1)
        quicksort_decrescente(herois, pivo + 1, fim)

def particionar(herois, inicio, fim):
    pivo = herois[fim].chave
    i = inicio - 1
    for j in range(inicio, fim):
        if herois[j].chave >= pivo:  
            i += 1
            herois[i], herois[j] = herois[j], herois[i]
    herois[i + 1], herois[fim] = herois[fim], herois[i + 1]
    return i + 1


def heapsort_crescente(herois):
    n = len(herois)
    for i in range(n // 2 - 1, -1, -1):
        heapify_crescente(herois, n, i)
    for i in range(n - 1, 0, -1):
        herois[0], herois[i] = herois[i], herois[0]
        heapify_crescente(herois, i, 0)

def heapsort_decrescente(herois):
    n = len(herois)
    for i in range(n // 2 - 1, -1, -1):
        heapify_decrescente(herois, n, i)
    for i in range(n - 1, 0, -1):
        herois[0], herois[i] = herois[i], herois[0]
        heapify_decrescente(herois, i, 0)

def heapify_crescente(herois, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and herois[esq].chave > herois[maior].chave:
        maior = esq
    if dir < n and herois[dir].chave > herois[maior].chave:
        maior = dir
    if maior != i:
        herois[i], herois[maior] = herois[maior], herois[i]
        heapify_crescente(herois, n, maior)

def heapify_decrescente(herois, n, i):
    menor = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and herois[esq].chave < herois[menor].chave:
        menor = esq
    if dir < n and herois[dir].chave < herois[menor].chave:
        menor = dir
    if menor != i:
        herois[i], herois[menor] = herois[menor], herois[i]
        heapify_decrescente(herois, n, menor)
 
def mergesort_crescente(herois):
    if len(herois) > 1:
        meio = len(herois) // 2
        esq = herois[:meio]
        dir = herois[meio:]
        mergesort_crescente(esq)
        mergesort_crescente(dir)
        merge_crescente(herois, esq, dir)

def mergesort_decrescente(herois):
    if len(herois) > 1:
        meio = len(herois) // 2
        esq = herois[:meio]
        dir = herois[meio:]
        mergesort_decrescente(esq)
        mergesort_decrescente(dir)
        merge_decrescente(herois, esq, dir)

def merge_crescente(herois, esq, dir):
    i = j = k = 0
    while i < len(esq) and j < len(dir):
        if esq[i].chave <= dir[j].chave:
            herois[k] = esq[i]
            i += 1
        else:
            herois[k] = dir[j]
            j += 1
        k += 1
    while i < len(esq):
        herois[k] = esq[i]
        i += 1
        k += 1
    while j < len(dir):
        herois[k] = dir[j]
        j += 1
        k += 1

def merge_decrescente(herois, esq, dir):
    i = j = k = 0
    while i < len(esq) and j < len(dir):
        if esq[i].chave >= dir[j].chave:
            herois[k] = esq[i]
            i += 1
        else:
            herois[k] = dir[j]
            j += 1
        k += 1
    while i < len(esq):
        herois[k] = esq[i]
        i += 1
        k += 1
    while j < len(dir):
        herois[k] = dir[j]
        j += 1
        k += 1
     
def preencheObj(obj, herois):

    for linha in obj:
        valores = linha.split("|")
        chave = int(valores[0])
        primeiroNome = valores[1]
        sobreNome = valores[2]
        nomeHeroi = valores[3]
        poder = valores[4]
        fraqueza = valores[5]
        cidade = valores[6]
        profissao = valores[7]

        # Crie uma instância do objeto Heroi com os valores lidos
        heroi = Heroi(chave, primeiroNome, sobreNome, nomeHeroi, poder, fraqueza, cidade, profissao)

        # Adicione o objeto Heroi à lista de herois
        herois.append(heroi)

    return herois

def gravar_saida(herois, arquivo_saida,sort  , order, size):
    with open(arquivo_saida, "w") as arquivo:
        arquivo.write("SIZE=" + str(size) + " TOP=-1 QTDE=" + str(len(herois)) + " SORT=" + sort + " ORDER=" + order + "\n")
        for heroi in herois:
            aux = heroi.profissao.replace("\n", " ")
            heroi.profissao = aux
            linha = f"{heroi.chave}|{heroi.primeiroNome}|{heroi.sobreNome}|{heroi.nomeHeroi}|{heroi.poder}|{heroi.fraqueza}|{heroi.cidade}|{heroi.profissao}\n"
            arquivo.write(linha)


if __name__ == "__main__":

    arq1 = sys.argv[1]
    arq2 = sys.argv[2]

    with open(arq1, 'r') as f1:
        linhas = f1.readlines()
        if os.stat(arq1).st_size == 0:
            print("Arquivo vazio!!")
            with open(arq2, "w") as arquivo:
                arquivo.write("Arquivo Inválido!(Vazio) \n")
                
            exit()
        topo = linhas[0]
        size = re.search(r'SIZE=(\d+)', linhas[0]).group(1)
        top = re.search(r'TOP=(-?\d+)', linhas[0]).group(1)
        qtde = re.search(r'QTDE=(\d+)', linhas[0]).group(1)
        sort = re.search(r'SORT=(\w+)', linhas[0]).group(1)
        order = re.search(r'ORDER=(\w+)', linhas[0]).group(1)
        herois = []
       
        preencheObj(linhas[1:], herois)
        chaves_herois = [heroi.chave for heroi in herois]
        if sort == "Q":
            if order == "C":
                ordenado = quicksort_crescente(herois, 0, len(herois) - 1)
            if order == "D":
                ordenado = quicksort_decrescente(herois, 0, len(herois) - 1)
            if order != "D" and order != "C":
                print("Ordenação inválida!")
                with open(arq2, "w") as arquivo:
                    arquivo.write("Arquivo Inválido! \n")
                exit()
                
        elif sort == "M":  
            if order == "C":
                mergesort_crescente(herois)
            if order == "D":    
                mergesort_decrescente(herois)
            if order != "D" and order != "C":
                print("Ordenação inválida!")
                with open(arq2, "w") as arquivo:
                    arquivo.write("Arquivo Inválido! \n")
                exit()
        elif sort == "I":
            if order == "C":
                insertionsort_crescente(herois)
            if order == "D":
                insertionsort_decrescente(herois)
            if order != "D" and order != "C":
                print("Ordenação inválida!")
                with open(arq2, "w") as arquivo:
                    arquivo.write("Arquivo Inválido! \n")
                exit()
                
        elif sort == "H":
            if order == "C":
                heapsort_crescente(herois)
            if order == "D":
                heapsort_decrescente(herois)
            if order != "D" and order != "C":
                print("Ordenação inválida!")
                with open(arq2, "w") as arquivo:
                    arquivo.write("Arquivo Inválido! \n")
                exit()
        elif sort != "Q" and sort != "M" and sort != "I" and sort != "H":
            print("Ordenação inválida!")
            with open(arq2, "w") as arquivo:
                arquivo.write("Arquivo Inválido! \n")
            exit()

        #print(topo, size, top, qtde, sort, order)
        gravar_saida(herois, arq2 , sort,order, size)

