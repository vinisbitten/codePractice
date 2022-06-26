from recurso import Recurso

class Cafeteira(Recurso):

    def __init__(self, nome):
        super().__init__(nome)

    def __repr__(self):
        str = super().__repr__()
        str += f', Tipo: {self.tipo}'
        return str

    def processa(self):
        print(f'>Recurso {self.nome} com processamento solicitado')

        if super().processa():
            print('>Tarefa processada')
            if self.ocupado == False:
                print(f'>Recurso {self.nome} liberado')
            print('>Fazendo cafe')
            print('>Cafe feito com sucesso')
        else:
            print('>Nao ha tarefas a serem processadas')
            print('>Cafeteira deve ser reservada previamente')
        
        print('')

class Impressora(Recurso):

    def __init__(self, nome):
        super().__init__(nome)

    def __repr__(self):
        str = super().__repr__()
        str += f', Tipo: {self.tipo}'
        return str
    
    def processa(self):
        print(f'>Recurso {self.nome} com processamento solicitado')

        if super().processa():
            print('>Tarefa processada')
            if self.ocupado == False:
                print(f'>Recurso {self.nome} liberado')
            print('>Realizando impressao')
            print('>Impressao realizada com sucesso')
        else:
            print('>Nao ha tarefas a serem processadas')
            print('>Impressora deve ser reservada previamente')
        
        print('')