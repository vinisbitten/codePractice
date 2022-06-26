from PreProcessador import PreProcessador
class ContadorPalavras(PreProcessador):
    def __init__(self, texto):
        PreProcessador.__init__(self, texto)
        self.ocorrencias = []
    def processa(self):
        PreProcessador.processa(self)
        self.ocorrencias.append(self.lista_palavras[0])

        for palavra in self.lista_palavras:
            if palavra not in self.ocorrencias:
                self.ocorrencias.append(palavra)
    def __str__(self):
        result = ''
        for palavra in self.ocorrencias:
            n = self.lista_palavras.count(palavra)
            result += f'{palavra}: {n} vezes\n'
        return result

if __name__ == '__main__':
    contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
                                ' Este texto possui vários termos repetidos:'
                                ' este, Este, ESte, esTE!')
    contador.processa()
    print(contador)