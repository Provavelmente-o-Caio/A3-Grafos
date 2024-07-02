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

            if "arcs" in linha:
                lendo_vertices = False
                lendo_arestas = True
                continue

            if lendo_vertices:
                index, rotulo = linha.split(maxsplit=1)
                self.vertices.append(Vertice(int(index), rotulo.strip()))
                continue

            if lendo_arestas:
                peso = 999999
                if len(linha.split()) == 2:
                    v1_index, v2_index, *args = linha.split()
                else:
                    v1_index, v2_index, peso = linha.split()
                v1 = self.vertices[int(v1_index)-1]
                v2 = self.vertices[int(v2_index)-1]

                if peso != 999999:
                    self.arestas.append(Aresta(v1, v2, peso))
                else:
                    self.arestas.append(Aresta(v1, v2))
                v1.add_aresta(v2)