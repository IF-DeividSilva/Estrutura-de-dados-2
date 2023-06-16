class NoBTree:
    def __init__(self, folha=False):
        self.folha = folha
        self.keys = []
        self.filho = []


class BTree:
    def __init__(self):
        self.root = NoBTree(folha=True)

    def inserir(self, chave):
        raiz = self.root
        if len(raiz.keys) == 5:
            temp = NoBTree()
            self.root = temp
            temp.filho.append(raiz)
            self.dividirFilho(temp, 0)
            self.inserirNaoCheio(temp, chave)
        else:
            self.inserirNaoCheio(raiz, chave)

    def inserirNaoCheio(self, x, chave):
        i = len(x.keys) - 1
        if x.folha:
            x.keys.append((None, None))
            while i >= 0 and chave < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = chave
        else:
            while i >= 0 and chave < x.keys[i]:
                i -= 1
            i += 1
            if len(x.filho[i].keys) == 5:
                self.dividirFilho(x, i)
                if chave > x.keys[i]:
                    i += 1
            self.inserirNaoCheio(x.filho[i], chave)

    def dividirFilho(self, x, i):
        y = x.filho[i]
        z = NoBTree(folha=y.folha)
        x.filho.insert(i + 1, z)
        x.keys.insert(i, y.keys[4])
        z.keys = y.keys[5:9]
        y.keys = y.keys[:4]
        if not y.folha:
            z.filho = y.filho[5:10]
            y.filho = y.filho[:5]

    def imprimirArvore(self, x=None, l=0):
        x = x or self.root

        if len(x.keys) > 0:
            print("Nível", l, "(", len(x.keys), "chaves):", end=" ")
            for chave in x.keys:
                print(chave, end=" ")
            print()

        l += 1
        if len(x.filho) > 0:
            for filho in x.filho:
                self.imprimirArvore(filho, l)

def main():
    # Criando uma instância da B-Tree
    b_tree = BTree()

    # Inserindo a sequência fornecida
    sequencia = [-6, -32, 68, 33, -1, 22, 62, -34, 90, -26, -95, 17, 44, 93, 76, -20, -56, 79, -74, -81]
    for chave in sequencia:
        b_tree.inserir(chave)

    # Imprimindo a árvore resultante
    b_tree.imprimirArvore()


if __name__ == '__main__':
    main()