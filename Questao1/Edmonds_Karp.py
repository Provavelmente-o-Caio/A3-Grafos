from src.GrafoDirigido import GrafoDirigido
from src.Aresta import Aresta
from src.Vertice import Vertice

class EdmondsKarp:
    def __init__(self, graph: GrafoDirigido):
        self.graph = graph
        self.V = self.graph.get_vertices()  # Obtém todos os vértices do grafo
        self.E = self.graph.get_arestas()  # Obtém todas as arestas do grafo

        # Cria uma cópia do grafo original para o grafo residual
        self.residual_graph_1 = graph

        # Lista para armazenar arestas invertidas com peso 0
        arestas_to_invert = []
        for E in self.E:
            # Adiciona arestas invertidas (v2 -> v1) com peso 0
            arestas_to_invert.append(Aresta(E.get_v2(), E.get_v1(), 0))

        # Cria o grafo residual com vértices e arestas invertidas
        self.residual_graph = GrafoDirigido(self.V, arestas_to_invert)

    def bfs(self, source, sink):
        # Inicializa os vértices como não visitados
        visited = {vertice: False for vertice in self.V}
        # Inicializa os ancestrais dos vértices
        ancestor = {vertice: False for vertice in self.V}
        queue = [source]
        visited[source] = True
        self.parent = {source: None}
        p = []

        while queue:
            u = queue.pop(0)

            # Verifica os vizinhos de 'u' no grafo residual
            for v in self.residual_graph_1.vizinhos(u.get_index()):
                # Verifica se o vértice 'v' não foi visitado e a aresta tem peso positivo
                if not visited[v] and int(self.residual_graph_1.get_aresta_uv(u.get_index(), v.get_index()).get_peso()) > 0:
                    queue.append(v)
                    visited[v] = True
                    ancestor[v] = u

                    if v == sink:
                        p = [sink]
                        w = sink
                        # Reconstrói o caminho a partir dos ancestrais
                        while w != source:
                            w = ancestor[w]
                            p.insert(0, w)
                        return p

        return []

    def edmonds_karp(self, source, sink):
        max_flow = 0

        while True:
            p = self.bfs(source, sink)  # Encontra um caminho de aumento

            if p == []:
                break

            path_flow = 99999999999999
            v = sink

            # Encontrar o fluxo máximo ao longo do caminho 'p'
            while v != source:
                u = p[p.index(v) - 1]  # Obtém o predecessor de 'v' no caminho 'p'
                path_flow = min(path_flow, int(self.residual_graph_1.get_aresta_uv(u.get_index(), v.get_index()).get_peso()))
                v = u

            max_flow += path_flow  # Atualiza o fluxo máximo

            # Atualiza as capacidades residuais das arestas no caminho 'p'
            v = sink
            while v != source:
                u = p[p.index(v) - 1]  # Obtém o predecessor de 'v' no caminho 'p'

                # Atualiza o peso da aresta (u, v) no grafo residual
                peso_uv = int(self.residual_graph_1.get_aresta_uv(u.get_index(), v.get_index()).get_peso())
                self.residual_graph_1.get_aresta_uv(u.get_index(), v.get_index()).set_peso(peso_uv - path_flow)

                # Atualiza o peso da aresta (v, u) no grafo residual
                peso_vu = int(self.residual_graph.get_aresta_uv(u.get_index(), v.get_index()).get_peso())
                self.residual_graph.get_aresta_uv(u.get_index(), v.get_index()).set_peso(peso_vu + path_flow)

                # Move para o próximo vértice no caminho
                v = u

        print(max_flow)
        return max_flow
