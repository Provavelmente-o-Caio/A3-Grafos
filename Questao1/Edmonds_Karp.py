from src.GrafoDirigido import GrafoDirigido
from src.Aresta import Aresta
from src.Vertice import Vertice

class EdmondsKarp:
    def __init__(self, graph: GrafoDirigido):
        self.graph = graph
        self.V = self.graph.get_vertices()
        self.E = self.graph.get_arestas()

        #Mesma coisa do primeiro grafo
        self.residual_graph_1 = graph

        arestas_to_invert = []
        for E in self.E:
            arestas_to_invert.append(Aresta(E.get_v2(),E.get_v1(),0))

        self.residual_graph = GrafoDirigido(self.V,arestas_to_invert)

    def bfs(self, source, sink):
        visited = {vertice: False for vertice in self.V}
        ancestor = {vertice: False for vertice in self.V }
        queue = [source]
        visited[source] = True
        self.parent = {source: None}
        p = []

        while queue:
            
            u = queue.pop(0)

            for v in self.residual_graph_1.vizinhos(u.get_index()):
                if not visited[v] and int(self.residual_graph_1.get_aresta_uv(u.get_index(),v.get_index()).get_peso()) > 0:
                    queue.append(v)
                    visited[v] = True
                    ancestor[v] = u

                    if v == sink:
                        p = [sink]
                        w = sink
                        while w != source:
                            w = ancestor[w]
                            p.insert(0, w)
                        return p

        return []
            

    def edmonds_karp(self, source, sink):

        max_flow = 0

        while True:

            p = self.bfs(source, sink)

            if p == []:
                break

            path_flow = 99999999999999
            v = sink

            # Encontrar o fluxo máximo ao longo do caminho p
            while v != source:
                u = p[p.index(v) - 1]  # Obtém o predecessor de 'v' no caminho 'p'
                path_flow = min(path_flow, int(self.residual_graph_1.get_aresta_uv(u.get_index(),v.get_index()).get_peso()))
                v = u 

            max_flow += path_flow

            # Atualizar as capacidades residuais das arestas no caminho p
            v = sink
            while v != source:
                u = p[p.index(v) - 1]  # Obtém o predecessor de 'v' no caminho 'p'

                # Atualiza o peso da aresta (u, v) no grafo residual
                peso_uv = int(self.residual_graph_1.get_aresta_uv(u.get_index(),v.get_index()).get_peso())
                self.residual_graph_1.get_aresta_uv(u.get_index(),v.get_index()).set_peso(peso_uv - path_flow)

                # Atualiza o peso da aresta (v, u) no grafo residual
                peso_vu = int(self.residual_graph.get_aresta_uv(u.get_index(),v.get_index()).get_peso())
                self.residual_graph.get_aresta_uv(u.get_index(),v.get_index()).set_peso(peso_vu + path_flow)

                # Move para o próximo vértice no caminho
                v = u

        print(max_flow)
        return max_flow