import string

class PreProcessador:
    def __init__(self, texto):
        self.texto = texto
        self.lista_palavras = []
    def __organiza(self):
        self.texto = self.texto.lower()
        self.texto = self.texto.translate(str.maketrans('', '', string.punctuation))
    def processa(self):
        self.__organiza()
        self.lista_palavras = self.texto.split(' ')

    def __str__(self):
        return str(self.lista_palavras)

if __name__ == '__main__':
    preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
                                     ' Este texto possui vários termos repetidos:'
                                     ' este, Este, ESte, esTE!')
    preprocessador.processa()
    print(preprocessador)