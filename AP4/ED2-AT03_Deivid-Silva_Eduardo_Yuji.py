import sys
import os

# Classe para representar uma música
class Musica:
    def __init__(self, ano, duracao, titulo, artista, genero, idioma):
        self.ano = ano
        self.duracao = duracao
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.idioma = idioma

def preencheObj(linhas, musicas):
    for linha in linhas:
        dados = linha.strip().split("|")
        if len(dados) == 6:
            ano = dados[0]
            duracao = dados[1]
            titulo = dados[2].casefold()
            artista = dados[3].casefold()
            generos = dados[4].split(" ")
            generos = [genero.casefold() for genero in generos]
            idioma = dados[5].casefold()

            musica = Musica(ano, duracao, titulo, artista, generos, idioma)
            musicas.append(musica)

def criar_indiceSecundario(musicas, tipoIndice):
    indice = {}
    for musica in musicas:
        if tipoIndice == 'ano':
            if musica.ano not in indice:
                indice[musica.ano] = []
            indice[musica.ano].append(musica)
        elif tipoIndice == 'titulo':
            if musica.titulo not in indice:
                indice[musica.titulo] = []
            indice[musica.titulo].append(musica)
        elif tipoIndice == 'artista':
            if musica.artista not in indice:
                indice[musica.artista] = []
            indice[musica.artista].append(musica)
        elif tipoIndice == 'genero':
            for genero in musica.genero:
                if genero not in indice:
                    indice[genero] = []
                indice[genero].append(musica)
        elif tipoIndice == 'idioma':
            if musica.idioma not in indice:
                indice[musica.idioma] = []
            indice[musica.idioma].append(musica)

    return indice

def consulta(indice, valor_consulta):
    valor_consulta = valor_consulta.casefold()
    if valor_consulta in indice:
        return indice[valor_consulta]
    else:
        return []

def gravarSaida(resultado, arq3):
    resultado_str = '\n'.join(resultado)
    with open(arq3, "w") as arquivo:
        if not resultado_str:
            arquivo.write("Nenhum registro foi encontrado!!\n")
        arquivo.write(resultado_str)


def main():
    arq1 = "musics.txt"  # sys.argv[1]
    arq2 = "entrada06.txt"  # sys.argv[2]
    arq3 = "saida.txt"  # sys.argv[3]

    with open(arq1, 'r') as f1:
        linhas = f1.readlines()
        if os.stat(arq1).st_size == 0:
            print("Arquivo vazio!!")
            with open(arq3, "w") as arquivo:
                arquivo.write("Arquivo Inválido! (Vazio)\n")
            exit()

        musicas = []
        preencheObj(linhas[1:], musicas)

    with open(arq2, 'r') as f2:
        tipoIndice = f2.readline().strip()
        if tipoIndice not in ['ano', 'titulo', 'artista', 'genero', 'idioma']:
            print('Tipo de índice inválido.')
            return

        palavra = f2.readline().strip()

        indice = criar_indiceSecundario(musicas, tipoIndice)
        resultado = consulta(indice, palavra)
        resultado_formatado = [f"{musica.ano}|{musica.duracao}|{musica.titulo}|{musica.artista}|{' '.join(musica.genero)}|{musica.idioma}" for musica in resultado]
        gravarSaida(resultado_formatado, arq3)

    print("Consulta concluída com sucesso!")

if __name__ == "__main__":
    main()
