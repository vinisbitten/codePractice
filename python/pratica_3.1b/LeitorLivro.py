from livro import Livro, ExcecaoSistema

class LeitorLivro():
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.livros = []
        self.arquivo = '.txt'

    def processa(self):
        with open(self.nome_arquivo, 'r') as self.arquivo:
            quantLivros = self.arquivo.readline()

            while quantLivros > 0:
                try:
                    l = Livro()
                    l.titulo = self.arquivo.readline()
                    l.ano = int(self.arquivo.readline())
                    l.isbn = self.arquivo.readline()
                except ExcecaoSistema as erro:
                    print(erro)
                else:
                    self.livros.append(l)
            quantLivros -= 1

if __name__ == '__main__':
    arq = input('Insira o nome do arquivo: ')
    le = LeitorLivro(arq)
    le.processa()

    for livro in le.livros:
        print(str(livro) + '\n')
