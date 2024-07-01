from src.Vertice import Vertice
from src.Aresta import Aresta
from math import inf as infinito


class Grafo:
    def __init__(self, vertices=None, arestas=None) -> None:
        if vertices is None:
            self.vertices = []
        else:
            self.vertices = vertices

        if arestas is None:
            self.arestas = []
        else:
            self.arestas = arestas

    def ler(self, caminho: str) -> None:
        pass

    def printGrafo(self) -> None:
        for v in self.vertices:
            v.printVertice()
        for a in self.arestas:
            a.printAresta()

    def qtdVertices(self) -> int:
        return len(self.vertices)

    def qtdArestas(self) -> int:
        return len(self.arestas)

    def grau(self, vertice: int) -> int:
        return len(self.vertices[vertice - 1].get_arestas())

    def rotulo(self, index: int) -> str:
        return self.vertices[index - 1].get_rotulo()

    def vizinhos(self, vertice: int) -> list[Vertice]:
        return list(self.vertices[vertice - 1].get_arestas().keys())

    def haAresta(self, u: int, v: int) -> bool:
        v1 = self.vertices[u - 1]
        v2 = self.vertices[v - 1]
        if v2.get_index() in v1.get_arestas().keys():
            return True
        else:
            return False

    def peso(self, u: int, v: int) -> float:
        v1 = self.vertices[u - 1]
        v2 = self.vertices[v - 1]
        if v2 in v1.get_arestas().keys():
            return float(v1.get_arestas()[v2])
        else:
            return infinito

    # Getters
    def get_vertices(self) -> list[Vertice]:
        return self.vertices

    def get_arestas(self) -> list[Aresta]:
        return self.arestas

    def get_aresta_uv(self, u: int, v: int) -> Aresta:
        pass