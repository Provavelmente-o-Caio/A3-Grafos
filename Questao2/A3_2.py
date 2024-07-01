from src.GrafoNaoDirigido import GrafoNaoDirigido
from math import inf
from queue import Queue

INF = 2147483647
NIL = 0

def hopcroftKarp(g: GrafoNaoDirigido):
    verticesDeCadaLado = g.qtdVertices() // 2
    x = [0 for _ in range(verticesDeCadaLado +1)]
    y = [0 for _ in range(verticesDeCadaLado +1)]

    distancias = [0 for _ in range(verticesDeCadaLado +1)]

    result = 0

    while bfs(g, x, y, distancias):
        for u in range(1,verticesDeCadaLado +1):
            if x[u] == NIL and dfs(g, x, y, u, distancias):
                result += 1

    print(result)

def bfs(g:GrafoNaoDirigido, x, y, distancias):
    Q = Queue()
    for u in range(1, g.qtdVertices()//2 + 1):
        if x[u] == NIL:
            distancias[u] = 0
            Q.put(u)
        else:
            distancias[u] = INF


    distancias[NIL] = INF

    while not Q.empty():
        u = Q.get()
        verticesCadaLado = g.qtdVertices() // 2

        if distancias[u] < distancias[NIL]:
            for v in g.vizinhos(u):
                v_num = v.get_index()
                if distancias[y[v_num - verticesCadaLado]] == INF:
                    distancias[y[v_num - verticesCadaLado]] = distancias[u] + 1
                    Q.put(y[v_num - verticesCadaLado])

    return distancias[NIL] != INF

def dfs(g:GrafoNaoDirigido, x, y, u, distancias):
    verticesCadaLado = g.qtdVertices() // 2
    if u != NIL:
        # Get all adjacent vertices of the dequeued vertex u
        for v in g.vizinhos(u):
            v_num = v.get_index()
            if distancias[y[v_num - verticesCadaLado]] == distancias[u] + 1:
                # If dfs for pair of v also returns true
                if dfs(g, x, y, y[v_num - verticesCadaLado], distancias):
                    y[v_num - verticesCadaLado] = u
                    x[u] = v_num
                    return True
        # If there is no augmenting path beginning with u.
        distancias[u] = INF
        return False
    return True