from PreProcessador import PreProcessador

class Tradutor(PreProcessador):
    def __init__(self, texto):
        PreProcessador.__init__(self, texto)
        self.traducoes = {
            'olá' : 'hello',
            'este' : 'this',
            'é' : 'is',
            'um' : 'a',
            'exemplo' : 'example',
            'de' : 'of',
            'texto' : 'text',
            'com' : 'with',
            'termos' : 'terms',
            'repetidos' : 'repeated',
            'possui' : 'has',
            'vários' : 'various'
        }
        self.lista_palavras_trad = []
    def processa(self):
        PreProcessador.processa(self)
        for palavra in self.lista_palavras:
            self.lista_palavras_trad.append(palavra.translate(self.traducoes))
    def __str__(self):
        return str(self.lista_palavras_trad)

if __name__ == '__main__':

    tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
                        ' Este texto possui vários termos repetidos:'
                        ' este, Este, ESte, esTE!')
    tradutor.processa()
    print(tradutor)