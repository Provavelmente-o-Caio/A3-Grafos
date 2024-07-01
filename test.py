from Questao2.A3_2 import hopcroftKarp
from src.GrafoNaoDirigido import GrafoNaoDirigido

grafo = GrafoNaoDirigido()
grafo.ler("Testes/testEmp.txt")

print("Questao 2")
hopcroftKarp(grafo)