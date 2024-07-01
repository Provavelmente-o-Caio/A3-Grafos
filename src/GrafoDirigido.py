from src.Grafo import Grafo
from src.Vertice import Vertice
from src.Aresta import Aresta

class GrafoDirigido(Grafo):
    def __init__(self, vertices=None, arestas=None) -> None:
        super().__init__(vertices, arestas)

    def ler(self, caminho: str) -> None:
        f = open(caminho, 'r')

        lendo_vertices = False
        lendo_arestas = False

        while True:
            linha = f.readline()
            if not linha:
                break

            if "vertices" in linha:
                lendo_vertices = True
                continue

            if "edges" in linha:
                lendo_vertices = False
                lendo_arestas = True
                continue

            if lendo_vertices:
                index, rotulo = linha.split(maxsplit=1)
                self.vertices.append(Vertice(int(index), rotulo.strip()))
                continue

            if lendo_arestas:
                v1_index, v2_index, *args = linha.split()
                v1 = self.vertices[int(v1_index)-1]
                v2 = self.vertices[int(v2_index)-1]

                self.arestas.append(Aresta(v1, v2))

                v1.add_aresta(v2)

    def add_aresta(self, aresta: Aresta):
        v = aresta.get_v1()
        u = aresta.get_v2()
        peso = aresta.get_peso()

        self.arestas.append(Aresta(v, u))

        v.add_aresta(u, peso)

    def set_peso(self, aresta: Aresta, peso: int):
        v = aresta.get_v1()
        u = aresta.get_v2()
        peso = aresta.get_peso()

        for aresta_existente in self.arestas:
            if aresta_existente == aresta:
                aresta_existente.set_peso(peso)

    def get_aresta_uv(self, u: int, v: int) -> Aresta:
        for aresta in self.arestas:
            if aresta.get_v1().get_index() == u and aresta.get_v2().get_index() == v:
                return aresta
