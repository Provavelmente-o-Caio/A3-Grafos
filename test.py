from Questao2.A3_2 import hopcroftKarp
from Questao3.A3_3 import lawler
from src.GrafoNaoDirigido import GrafoNaoDirigido

#grafo = GrafoNaoDirigido()
#grafo.ler("Testes/testEmp.txt")

#print("Questao 2")
#hopcroftKarp(grafo)

grafo3 = GrafoNaoDirigido()
grafo3.ler("Testes/testeCor.txt")

print("Questao 3")
lawler(grafo3)
