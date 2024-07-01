import sys
from src.GrafoNaoDirigido import GrafoNaoDirigido
from src.GrafoDirigido import GrafoDirigido
from Questao1.A3_1 import fluxo_maximo

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python main.py nome_do_arquivo numero_da_questao")
        print("OBS: arquivo deve estar no diretório 'Testes'")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    nome_algoritmo = sys.argv[2]

    grafo_dirigido = GrafoDirigido()
    grafo_nao = GrafoNaoDirigido()

    try:
        grafo_dirigido.ler("Testes/" + nome_arquivo)
        grafo_nao.ler("Testes/" + nome_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")

    if nome_algoritmo != 'ALL' and (not nome_algoritmo.isdigit() or int(nome_algoritmo) > 3 or int(nome_algoritmo) < 1):
        print("O número da questão deve estar entre os valores para a entrega. Ou ALL para rodar todas as questões")
        sys.exit(1)

    if nome_algoritmo == "1" or nome_algoritmo == "ALL":
        print()
        print("Edmonds Karp")
        print()
        print(fluxo_maximo(grafo_dirigido, grafo_dirigido.get_vertices()[0], grafo_dirigido.get_vertices()[grafo_dirigido.qtdVertices()-1]))

    if nome_algoritmo == "2" or nome_algoritmo == "ALL":
        print()
        print("Hopcroft-Karp")
        print()

    if nome_algoritmo == "3" or nome_algoritmo == "ALL":
        print()
        print("Coloração de Vértices")
        print()