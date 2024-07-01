import sys
from src.GrafoNaoDirigido import GrafoNaoDirigido
from src.GrafoDirigido import GrafoDirigido
from Questao1.Edmonds_Karp import EdmondsKarp
#from Questao2.Hopcroft_Karp import Hopcroft_Karp
#from Questao3.Lawler import Lawler

'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python main.py nome_do_arquivo numero_da_questao")
        print("OBS: arquivo deve estar no diretório 'Testes'")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    nome_algoritmo = sys.argv[2]
'''
nome_arquivo = "oii.txt"
grafo_dirigido = GrafoDirigido()
grafo_nao = GrafoNaoDirigido()

try:
    grafo_dirigido.ler("./A3-Grafos/Testes/oii.txt")
except FileNotFoundError:
    print("Arquivo não encontrado")

#if nome_algoritmo != 'ALL' and (not nome_algoritmo.isdigit() or int(nome_algoritmo) > 5 or int(nome_algoritmo) < 1):
#   print("O número da questão deve estar entre os valores para a entrega. Ou ALL para rodar todas as questões")
#    sys.exit(1)

#if nome_algoritmo == "1" or nome_algoritmo == "ALL":
print()
print("Fluxo Máximo")
print()
ed = EdmondsKarp(grafo_dirigido)
s = None
t = None
for V in grafo_dirigido.get_vertices():
    if V.get_rotulo() == 's':
        s = V
    elif V.get_rotulo() == 't':
        t = V

ed.edmonds_karp(s, t)
'''
if nome_algoritmo == "2" or nome_algoritmo == "ALL":
    print()
    print("Ordenação Topológica")
    print()
    Hopcroft_Karp(grafo_dirigido)

if nome_algoritmo == "3" or nome_algoritmo == "ALL":
    print()
    print("Prim")
    print()
    Lawler(grafo_nao)'''