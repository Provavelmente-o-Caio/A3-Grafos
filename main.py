import sys
from src.GrafoNaoDirigido import GrafoNaoDirigido
from src.GrafoDirigido import GrafoDirigido
from Questao1.A3_1 import EdmondsKarp
from Questao2.A3_2 import hopcroftKarp
from Questao3.A3_3 import lawler

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python main.py nome_do_arquivo numero_da_questao")
        print("OBS: arquivo deve estar no diretório 'Testes'")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    nome_algoritmo = sys.argv[2]

    grafo_dirigido = GrafoDirigido()
    grafo_nao = GrafoNaoDirigido()

    if nome_algoritmo != 'ALL' and (not nome_algoritmo.isdigit() or int(nome_algoritmo) > 3 or int(nome_algoritmo) < 1):
        print("O número da questão deve estar entre os valores para a entrega. Ou ALL para rodar todas as questões")
        sys.exit(1)

    if nome_algoritmo == "1" or nome_algoritmo == "ALL":
        try:
            grafo_dirigido.ler("Testes/" + nome_arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado")

        print()
        print("Edmonds-Karp")
        print()
        ed = EdmondsKarp(grafo_dirigido)
        v = grafo_dirigido.get_vertices()
        s = v[0]
        t = v[len(v)-1]
        ed.edmonds_karp(s, t)


    if nome_algoritmo == "2" or nome_algoritmo == "ALL":
        try:
            grafo_nao.ler("Testes/" + nome_arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado")
    
        print()
        print("Hopcroft-Karp")
        print()
        hopcroftKarp(grafo_nao)

    if nome_algoritmo == "3" or nome_algoritmo == "ALL":
        try:
            grafo_nao.ler("Testes/" + nome_arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado")

        print()
        print("Coloração de Vértice")
        print()
        print(lawler(grafo_nao))