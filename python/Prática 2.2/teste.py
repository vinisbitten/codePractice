from gerenciador_recursos import GerenciadorRecursos
from classes_teste import Cafeteira, Impressora

if __name__ == "__main__":
    g = GerenciadorRecursos()
    r1 = Cafeteira('cafeteira1')
    r2 = Cafeteira('cafeteira2')
    r3 = Impressora('impressora1')
    r4 = Impressora('impressora2')
    g.adiciona(r1)
    g.adiciona(r2)
    g.adiciona(r3)
    g.adiciona(r4)
    print('>>> Estado Inicial:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 1)
    g.reserva('Impressora', 1)
    print('\n>>> Após reservar:')
    g.imprime_recursos()
    print('')

    g.processa_todos()
    print('\n>>> Após processar tarefas:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 5)
    g.reserva('Cafeteira', 1)
    g.libera('cafeteira1')
    print('\n>>> Após reservar e liberar:')
    g.imprime_recursos()
    print('')
    g.libera('cafeteira1')