from biblioteca import Biblioteca, ErrPar, IsbnRepetido
from livro import ErroAno, ErroISBN, ErroTitulo, Livro

if __name__ == '__main__':
    biblioteca = Biblioteca()

    QuantLivros = int(input('Digite a quantidade de livros:'))

    while QuantLivros > 0:
        try:
            n = Livro()
            n.titulo = input('Digite o título do livro:')
            n.ano = int(input('Digite o ano do livro:'))
            n.isbn = input('Digite o ISBN do livro:')
        except ErroTitulo as ErrTit:
            print(ErrTit)
            n.titulo = input('Insira um novo título para o livro:')
        except ErroAno as ErrAn:
            print(ErrAn)
            n.ano = int(input('Insira uma novo ano para o livro:'))
        except ErroISBN as ErrIS:
            print(ErrIS)
            n.isbn = input('Insira um novo ISBN para o livro:')
        else:
            try:
                biblioteca.cadastra(n)
            except IsbnRepetido as IsRep:
                print(IsRep)
            except ErrPar as ErPar:
                print(ErrPar)
        QuantLivros -= 1
    
    #O Pequeno Príncipe
    #1943
    #978015
