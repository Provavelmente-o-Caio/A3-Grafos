from src.GrafoDirigido import GrafoDirigido
from src.Aresta import Aresta
from src.Vertice import Vertice
from math import inf as infinito

def ford_fulkerson(g: GrafoDirigido, s: Vertice, t: Vertice):
    # Configurando todos os vértices
    visitados = [False] * g.qtdVertices()
    ancestrais = [None] * g.qtdVertices()

    # Preparando a fila de visitas
    fila = []
    fila.append(s)

    # Configurando vértice de origem
    visitados[s.get_index()-1] = True

    # Iniciando a busca pela fonte
    while len(fila) != 0:
        u = fila.pop(0)
        print(g.vizinhos(u.get_index()))
        for vizinho in g.vizinhos(u.get_index()):
            peso = g.get_aresta_uv(u.get_index(), vizinho.get_index()).get_peso()
            print("Peso: ", peso)
            if not visitados[vizinho.get_index()-1] and peso > 0:
                visitados[vizinho.get_index()-1] = True
                ancestrais[vizinho.get_index()-1] = u
                # somedouro encontrado, criar o caminho aumentante
                if vizinho == t:
                    caminho_aumentante = []
                    caminho_aumentante.append(vizinho)
                    w = t
                    while w != s:
                        w = ancestrais[w.get_index()-1]
                        caminho_aumentante = [w] + caminho_aumentante
                    return caminho_aumentante
                fila.append(vizinho)
    return None

def fluxo_maximo(g: GrafoDirigido, s: Vertice, t: Vertice):
    # identificando a capacioade do caminho e adicionando ao fluxo total
    fluxo_total = 0
    caminho_aumentante = ford_fulkerson(g, s, t)
    while caminho_aumentante is not None:
        fluxo_local = capacidade_residual(g, caminho_aumentante)
        fluxo_total += fluxo_local

        # criando rede residual
        arestas = []
        for index in range(len(caminho_aumentante)-1):
            u = caminho_aumentante[index]
            v = caminho_aumentante[index+1]
            print("U: ", u.get_index())
            print("V: ", v.get_index())
            peso = g.get_aresta_uv(u.get_index(), v.get_index()).get_peso()
            print(peso)
            nova_aresta = Aresta(v, u, peso)
            g.add_aresta(nova_aresta)
            arestas.append(nova_aresta)


        # atualizando a capacidade residual
        for aresta in arestas:
            v = aresta.get_v1()
            u = aresta.get_v2()
            peso = aresta.get_peso()


            vu = g.get_aresta_uv(v.get_index(), u.get_index())
            uv = g.get_aresta_uv(u.get_index(), v.get_index())
            print("Peso UV: ", uv)
            print("Peso VU: ", vu)

            g.set_peso(uv, uv.get_peso() - fluxo_local)
            g.set_peso(vu, uv.get_peso() + fluxo_local)


        caminho_aumentante = ford_fulkerson(g, s, t)

    return fluxo_total

def capacidade_residual(g: GrafoDirigido, caminho_aumentante):
    menor = infinito
    for index in range(len(caminho_aumentante)-1):
        vertice = caminho_aumentante[index]
        proximo_vertice = caminho_aumentante[index+1]
        peso = g.get_aresta_uv(vertice.get_index(), proximo_vertice.get_index()).get_peso()
        if peso < menor:
            menor = peso
    return menor