from src.GrafoNaoDirigido import GrafoNaoDirigido
from math import inf
from queue import Queue

NIL = 0

def hopcroftKarp(g: GrafoNaoDirigido):
    vertices_g = g.get_vertices()
    x = vertices_g[:len(vertices_g)//2]

    distancias = [inf] * g.qtdVertices()
    mate = [None] * g.qtdVertices()

    # Tamanho do emparelhamento
    m = 0

    while bfs(g, mate, distancias):
        for vx in x:
            if mate[vx.get_index()-1] is None:
                if dfs(g, mate, vx, distancias):
                    m += 1

    print(m)
    print(mate)

def bfs(g:GrafoNaoDirigido, mate, distancias):
    vertices_g = g.get_vertices()
    x = vertices_g[:len(vertices_g)//2]
    y = vertices_g[len(vertices_g)//2:]

    q = Queue()
    for vx in x:
        if mate[vx.get_index()-1] is None:
            distancias[vx.get_index()-1] = 0
            q.put(vx)
        else:
            distancias[vx.get_index()-1] = inf

    # D_null
    distancias.append(inf)

    while not q.empty():
        vx = q.get()
        if distancias[vx.get_index()-1] < distancias[-1]:
            for vy in g.vizinhos(vx.get_index()):
                if mate[vy.get_index()-1] is not None:
                    if distancias[mate[vy.get_index()-1]] == inf:
                        distancias[mate[vy.get_index()-1]] = distancias[vx.get_index()-1] + 1
                        q.put(mate[vy.get_index()-1])

    return distancias[-1] != inf

def dfs(g:GrafoNaoDirigido, mate, vx, distancias):
    if vx is not None:
        for vy in g.vizinhos(vx.get_index()):
            if distancias[mate[vy.get_index()-1]] == distancias[vx.get_index()-1] + 1:
                if dfs(g, mate, mate[vy.get_index()-1], distancias):
                    mate[vy.get_index()-1] = vx
                    mate[vx.get_index()-1] = vy
                    return True

        distancias[vx.get_index()-1] = inf
        return False

    return True