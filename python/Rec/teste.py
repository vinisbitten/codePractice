from treino import *
from treinomovel import TreinoMovel
from treinorepeticao import TreinoRepeticao
from usuario import Usuario

if __name__ == '__main__':
    u1 = Usuario('Joao', 30, 82)
    print(u1)

    t1 = TreinoMovel('corrida', [360, 358, 362, 365, 355])
    t1.inicio = datetime.datetime(2021, 1, 6, 16, 0, 0)
    t1.fim = datetime.datetime(2021, 1, 6, 16, 30, 0)

    t2 = TreinoRepeticao('abdominais', [6, 7, 8, 7, 7, 6, 6, 8, 8, 7])
    t2.inicio = datetime.datetime(2021, 2, 28, 16, 45, 0)
    t2.fim = datetime.datetime(2021, 2, 28, 17, 00, 0)

    u1.adiciona_treino(t1)
    u1.adiciona_treino(t2)
    print('Lista de Treinos:')
    u1.imprime_calorias()

    u2 = Usuario('Cintia', 28, 60)
    print(u2)

    t3 = TreinoMovel('corrida', [350, 350, 355, 352, 351])
    t3.inicio = datetime.datetime(2021, 1, 21, 20, 15, 0)
    t3.fim = datetime.datetime(2021, 1, 21, 20, 45, 0)

    u2.adiciona_treino(t3)
    print('Lista de Treinos:')
    u2.imprime_calorias()

    print('t1 > t3: ' + str(TreinoMovel.compara(t1, t3)))