from ContadorDePalavras import ContadorPalavras
from Tradutor import Tradutor

class ProcessadorTexto(ContadorPalavras, Tradutor):
    def __init__(self, texto):
        ContadorPalavras.__init__(self, texto)
        Tradutor.__init__(self, texto)
    def processa(self):
        ContadorPalavras.processa(self)
        result = ''
        for palavra in self.ocorrencias:
            n = self.lista_palavras.count(palavra)
            result += f'{palavra}: {n} vezes\n'
        print(result)

        Tradutor.processa(self)
        trad = ''
        for palavra in self.lista_palavras_trad:
            trad += palavra + ' '
        print(trad)

if __name__ == '__main__':
    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    processadortexto.processa()