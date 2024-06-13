import sys
from src.GrafoNaoDirigido import GrafoNaoDirigido
from src.GrafoDirigido import GrafoDirigido
from Questao1.CFC import CFC
from Questao2.ordenacaoTopologica import ordenacaoTopologica
from Questao3.Prim import Prim

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

    if nome_algoritmo != 'ALL' and (not nome_algoritmo.isdigit() or int(nome_algoritmo) > 5 or int(nome_algoritmo) < 1):
        print("O número da questão deve estar entre os valores para a entrega. Ou ALL para rodar todas as questões")
        sys.exit(1)

    if nome_algoritmo == "1" or nome_algoritmo == "ALL":
        print()
        print("Componentes Fortemente Conexas")
        print()
        CFC(grafo_dirigido)

    if nome_algoritmo == "2" or nome_algoritmo == "ALL":
        print()
        print("Ordenação Topológica")
        print()
        ordenacaoTopologica(grafo_dirigido)

    if nome_algoritmo == "3" or nome_algoritmo == "ALL":
        print()
        print("Prim")
        print()
        Prim(grafo_nao)